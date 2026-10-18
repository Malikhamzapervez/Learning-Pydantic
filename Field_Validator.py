
from pydantic import BaseModel, EmailStr, AnyUrl, field_validator
from typing import List, Dict


class Patient1(BaseModel):
    name: str
    age: int
    Email: EmailStr
    Height: float
    Weight: float
    Linkedin_url: AnyUrl
    married: bool
    allergies: List[str]
    Contact: Dict[str, str]

    @field_validator("Email")
    @classmethod
    def validate_email(cls, value: EmailStr):
        valid_domains = [
            "edu.com",
            "yahoo.com",
            "outlook.com",
            "hotmail.com"
        ]

        domain = str(value).split("@")[-1].lower()

        if domain not in valid_domains:
            raise ValueError("Invalid email domain")

        return value

    @field_validator("age", mode="after" )# "before" # Field validator for age field, mode="before" means that the validation will be done before the value is assigned to the field
    @classmethod 
    def validate_age(cls, value:int):
        if 0 < value < 100:
            return value
        raise ValueError("Age must be between 0 and 100")

def insert(patient: Patient1):
    print(f"Name: {patient.name} and Age: {patient.age} are valid")
    print(f"Email: {patient.Email}")
    print(f"Contact: {patient.Contact}")
    print(f"Height: {patient.Height}")
    print(f"Weight: {patient.Weight}")
    print(f"LinkedIn URL: {patient.Linkedin_url}")
    print(f"Married: {patient.married}")
    print(f"Allergies: {patient.allergies}")


def update(patient: Patient1):
    print(f"Name: {patient.name} and Age: {patient.age} are updated")


patient = {
    "name": "John",
    "age": "25",
    "Height": 5.9,
    "Weight": 70.5,
    "Email": "john@edu.com",
    "married": False,
    "allergies": ["pollen", "dust"],
    "Contact": {"phone": "123-456-7890"},
    "Linkedin_url": "https://www.linkedin.com/in/john-doe"
}

patient_obj = Patient1(**patient)

insert(patient_obj)
