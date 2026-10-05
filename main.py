from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr, Field

from database import engine, Base, SessionLocal
from models import Employee, Department


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Cloud-Based Employee Management System",
    description="Simple Employee Management REST API",
    version="1.0.0"
)


# ============================================================
# DATABASE
# ============================================================

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine)


# ============================================================
# PYDANTIC SCHEMAS
# ============================================================

class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    salary: float = Field(gt=0)
    department_id: int | None = Field(default=None, gt=0)


class DepartmentCreate(BaseModel):
    department_name: str = Field(
        min_length=2,
        max_length=100
    )


class DepartmentResponse(BaseModel):
    department_id: int
    department_name: str


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    salary: float
    department_id: int | None
    department: DepartmentResponse | None


# ============================================================
# GET ALL / SINGLE EMPLOYEES
# ============================================================

@app.get(
    "/employees",
    response_model=list[EmployeeResponse]
)
def get_employees(
    employee_id: int | None = None,
    db=Depends(get_db)
):

    if employee_id is not None:

        employee = db.query(Employee).filter(
            Employee.id == employee_id
        ).first()

        if employee is None:
            raise HTTPException(
                status_code=404,
                detail="Employee not found"
            )

        return [employee]

    employees = db.query(Employee).all()

    return employees


# ============================================================
# CREATE EMPLOYEE
# ============================================================

@app.post(
    "/employees",
    response_model=EmployeeResponse
)
def create_employee(
    employee: EmployeeCreate,
    db=Depends(get_db)
):

    # Check duplicate email
    existing_employee = db.query(Employee).filter(
        Employee.email == employee.email
    ).first()

    if existing_employee is not None:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Check department
    if employee.department_id is not None:

        department = db.query(Department).filter(
            Department.department_id == employee.department_id
        ).first()

        if department is None:

            raise HTTPException(
                status_code=404,
                detail="Department not found"
            )

    new_employee = Employee(
        name=employee.name,
        email=employee.email,
        salary=employee.salary,
        department_id=employee.department_id
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


# ============================================================
# DELETE EMPLOYEE
# ============================================================

@app.delete(
    "/employees/{employee_id}"
)
def delete_employee(
    employee_id: int,
    db=Depends(get_db)
):

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee is None:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db.delete(employee)
    db.commit()

    return {
        "message": "Employee deleted successfully"
    }


# ============================================================
# CREATE DEPARTMENT
# ============================================================

@app.post(
    "/departments",
    response_model=DepartmentResponse
)
def create_department(
    department: DepartmentCreate,
    db=Depends(get_db)
):

    existing_department = db.query(Department).filter(
        Department.department_name ==
        department.department_name
    ).first()

    if existing_department is not None:

        raise HTTPException(
            status_code=400,
            detail="Department already exists"
        )

    new_department = Department(
        department_name=department.department_name
    )

    db.add(new_department)
    db.commit()
    db.refresh(new_department)

    return new_department


# ============================================================
# GET EMPLOYEES BY DEPARTMENT
# ============================================================

@app.get(
    "/departments/{department_id}/employees"
)
def get_employees_by_department(
    department_id: int,
    db=Depends(get_db)
):

    department = db.query(Department).filter(
        Department.department_id == department_id
    ).first()

    if department is None:

        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    employees = db.query(Employee).filter(
        Employee.department_id == department_id
    ).all()

    return employees
