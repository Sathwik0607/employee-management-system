from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    salary = Column(DECIMAL(10, 2), nullable=False, default=0)
    department_id = Column(
        Integer,
        ForeignKey("departments.department_id"),
        nullable=True
    )

    department = relationship("Department", back_populates="employees")


class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String(100), nullable=False)

    employees = relationship("Employee", back_populates="department")