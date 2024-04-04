from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from validators import validate_birth_date, validate_email, validate_name


Base = declarative_base()


class Department(Base):
    __attrs__ = ["id", "name"]
    __tablename__ = "department"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    employees = relationship(
        "Employee",
        back_populates="department",
        cascade="all, delete",
    )

    @staticmethod
    def validate_name(name):
        validate_name(name)


class Employee(Base):
    __attrs__ = [
        "id",
        "first_name",
        "last_name",
        "birth_date",
        "gender",
        "email",
        "role",
        "salary",
        "department_id",
    ]
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
    birth_date = Column(Date)
    gender = Column(String(1))
    email = Column(String(254))
    role = Column(String(50))
    salary = Column(Float)
    department_id = Column(Integer, ForeignKey("department.id"))
    department = relationship("Department", back_populates="employees")

    @staticmethod
    def validate_first_name(first_name):
        validate_name(first_name)

    @staticmethod
    @staticmethod
    def validate_last_name(last_name):
        validate_name(last_name)

    @staticmethod
    def validate_birth_date(birth_date):
        validate_birth_date(birth_date)

    @staticmethod
    def validate_email(email):
        validate_email(email)
