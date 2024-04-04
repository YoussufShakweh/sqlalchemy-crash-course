from tabulate import tabulate
from database import Session
from models import Department, Employee


def read_all_departments(session):
    departments = session.query(Department).all()
    table = [Department.__attrs__]
    for department in departments:
        table.append([department.id, department.name])

    print(tabulate(table, tablefmt="grid"))


def read_all_employees(session):
    employees = session.query(Employee).all()
    table = [Employee.__attrs__]
    for employee in employees:
        table.append(
            [
                employee.id,
                employee.first_name,
                employee.last_name,
                employee.birth_date,
                employee.gender,
                employee.email,
                employee.role,
                employee.salary,
                employee.department_id,
            ]
        )
    print(tabulate(table, tablefmt="grid"))


def main():
    session = Session()

    read_all_employees(session)

    session.close()


if __name__ == "__main__":
    main()
