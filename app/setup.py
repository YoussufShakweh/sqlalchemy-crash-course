"""
Run this file only once.
"""

import random
from faker import Faker
from database import engine, Session
from models import Base, Department, Employee

fake = Faker()
Base.metadata.create_all(engine)

GENDER_CHOICES = ["M", "F"]
ROLE_CHOICES = ["Admin", "Developer", "Assitant", "Product manager", "SCRUM master"]


def generate_departments(session) -> None:
    departments = ["AI", "Software", "Network"]
    for name in departments:
        department = Department(name=name)
        session.add(department)


def generate_employees(session) -> None:
    departments = session.query(Department).all()
    for _ in range(100):
        first_name = fake.first_name()
        last_name = fake.last_name()
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=65)
        gender = random.choice(GENDER_CHOICES)
        email = fake.email()
        role = random.choice(ROLE_CHOICES)
        salary = round(random.uniform(3000, 5000), 2)
        department = random.choice(departments)

        employee = Employee(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            gender=gender,
            email=email,
            role=role,
            salary=salary,
            department=department,
        )
        session.add(employee)


def main() -> None:
    session = Session()

    try:
        generate_departments(session)
        generate_employees(session)
        session.commit()
        print("Data generation completed successfully")
    except Exception as e:
        print(f"Error: {e}")

    session.close()


if __name__ == "__main__":
    main()
