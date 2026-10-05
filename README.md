\# Cloud-Based Employee Management System



A simple cloud-based Employee Management System built using \*\*Python, FastAPI, MySQL, Docker, and AWS\*\*. The application provides REST APIs for managing employees and departments and is deployed on AWS using \*\*EC2 and RDS\*\*.



\## Features



\* Create employees

\* Retrieve all employees

\* Retrieve a specific employee

\* Delete employees

\* Create departments

\* Retrieve employees by department

\* MySQL database for persistent data storage

\* Dockerized FastAPI application

\* AWS EC2 deployment

\* AWS RDS MySQL database

\* IAM-based EC2 permissions

\* GitHub Actions CI/CD deployment



\## Technologies Used



\### Backend



\* Python

\* FastAPI

\* SQLAlchemy

\* Pydantic



\### Database



\* MySQL

\* AWS RDS



\### Cloud \& Deployment



\* AWS EC2

\* AWS IAM

\* AWS Security Groups

\* Docker

\* GitHub Actions

\* Git/GitHub



\## Architecture



```text

&#x20;                        Internet

&#x20;                           |

&#x20;                           v

&#x20;                    GitHub Actions

&#x20;                           |

&#x20;                           | CI/CD

&#x20;                           v

&#x20;                     AWS EC2 Server

&#x20;                    +--------------+

&#x20;                    |    Docker    |

&#x20;                    |   FastAPI    |

&#x20;                    +------+-------+

&#x20;                           |

&#x20;                           | Database Connection

&#x20;                           v

&#x20;                      AWS RDS MySQL

&#x20;                           |

&#x20;                           v

&#x20;                   Employee Database



&#x20;             AWS IAM → EC2 Permissions

&#x20;             Security Groups → Network Access

```



\## Application Flow



```text

Client

&#x20; |

&#x20; v

FastAPI REST API

&#x20; |

&#x20; v

SQLAlchemy ORM

&#x20; |

&#x20; v

AWS RDS MySQL

```



The FastAPI application runs inside a Docker container on AWS EC2. SQLAlchemy is used to communicate with the MySQL database hosted on AWS RDS.



\## API Endpoints



\### Employees



| Method | Endpoint                      | Description             |

| ------ | ----------------------------- | ----------------------- |

| GET    | `/employees`                  | Get all employees       |

| GET    | `/employees?employee\_id={id}` | Get a specific employee |

| POST   | `/employees`                  | Create an employee      |

| DELETE | `/employees/{employee\_id}`    | Delete an employee      |



\### Departments



| Method | Endpoint                                 | Description                             |

| ------ | ---------------------------------------- | --------------------------------------- |

| POST   | `/departments`                           | Create a department                     |

| GET    | `/departments/{department\_id}/employees` | Get employees belonging to a department |



\## Example Employee Request



```json

{

&#x20; "name": "Test Employee",

&#x20; "email": "test.employee@gmail.com",

&#x20; "salary": 55000,

&#x20; "department\_id": 1

}

```



\## Database Design



\### Employees



\* `id` — Primary Key

\* `name`

\* `email`

\* `salary`

\* `department\_id` — Foreign Key



\### Departments



\* `department\_id` — Primary Key

\* `department\_name`



The `department\_id` in the employees table establishes a relationship between employees and departments.



\## Docker



The application is packaged as a Docker image.



```text

Dockerfile

&#x20;   |

&#x20;   v

Docker Image

&#x20;   |

&#x20;   v

Docker Container

&#x20;   |

&#x20;   v

FastAPI Application

```



The container exposes port `8000`, while AWS EC2 exposes the application through HTTP port `80`.



\## AWS Deployment



The application is deployed using the following architecture:



\* \*\*EC2\*\* — Hosts the Dockerized FastAPI application

\* \*\*RDS\*\* — Hosts the MySQL database

\* \*\*IAM\*\* — Provides permissions to the EC2 instance

\* \*\*Security Groups\*\* — Control network access

\* \*\*Environment Variables\*\* — Store database configuration securely



\## CI/CD



GitHub Actions is used to automate deployment.



```text

Developer

&#x20;   |

&#x20;   | git push

&#x20;   v

GitHub Repository

&#x20;   |

&#x20;   v

GitHub Actions

&#x20;   |

&#x20;   | SSH

&#x20;   v

AWS EC2

&#x20;   |

&#x20;   +--> Pull latest code

&#x20;   |

&#x20;   +--> Build Docker image

&#x20;   |

&#x20;   +--> Stop old container

&#x20;   |

&#x20;   +--> Start new container

&#x20;   |

&#x20;   v

Updated Application

```



Every push to the `main` branch triggers the deployment workflow.



\## Project Structure



```text

employee-management-system/

│

├── .github/

│   └── workflows/

│       └── deploy.yml

│

├── database.py

├── models.py

├── main.py

├── Dockerfile

├── requirements.txt

├── .dockerignore

├── .gitignore

└── README.md

```



\## Running Locally



\### 1. Clone the repository



```bash

git clone https://github.com/Sathwik0607/employee-management-system.git

cd employee-management-system

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



\### 3. Activate the environment



Windows:



```powershell

venv\\Scripts\\activate

```



\### 4. Install dependencies



```bash

pip install -r requirements.txt

```



\### 5. Configure database environment variables



Create a `.env` file containing the required database configuration.



```text

DB\_USER=your\_username

DB\_PASSWORD=your\_password

DB\_HOST=your\_database\_host

DB\_NAME=employee\_management

```



Do not commit the `.env` file to GitHub.



\### 6. Start the application



```bash

python -m uvicorn main:app --reload

```



The API will be available at:



```text

http://127.0.0.1:8000

```



Swagger documentation:



```text

http://127.0.0.1:8000/docs

```



\## Deployment



The application can be deployed using Docker and AWS EC2.



```bash

docker build -t employee-management-api .

```



```bash

docker run -d --name employee-management-container -p 80:8000 --env-file .env employee-management-api

```



\## Security



\* Database credentials are stored using environment variables.

\* `.env` is excluded from Git using `.gitignore`.

\* AWS IAM roles are used instead of storing AWS access keys on the EC2 server.

\* AWS Security Groups control inbound network access.

\* Database access is restricted through security-group rules.



\## Future Improvements



Possible future improvements include:



\* Automated testing

\* Improved authentication

\* Advanced monitoring

\* Load balancing

\* Infrastructure as Code

\* Automated rollback



\## Author



\*\*Sathwik\*\*



Cloud Engineering Project — 2026



