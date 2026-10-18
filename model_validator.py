
from pydantic import BaseModel, model_validator, computed_field



class Patient2(BaseModel):
    name: str
    age: int
    Email: str
    Height: float
    Weight: float
    Linkedin_url: str
    married: bool
    allergies: list[str]
    Contact: dict[str, str]


    @computed_field
    @property
    def bmi(self) -> float:
        return self.Weight / (self.Height ** 2)

    @model_validator(mode="after")
    def validate_contact(self):
        if self.age > 60 and "emergency" not in self.Contact:
            raise ValueError(
                "Emergency contact is required for patients over 60"
            )
        return self


def insert(patient: Patient2):
    print(f"Name: {patient.name} and Age: {patient.age} are valid")
    print(f"Contact: {patient.Contact}")
    print(f"BMI: {patient.bmi}")

patient = {
    "name": "John",
    "age": "20",
    "Height": 5.9,
    "Weight": 70.5,
    "Email": "john@edu.com",
    "married": False,
    "allergies": ["pollen", "dust"],
    "Contact": {"phone": "123-456-7890"},
    "Linkedin_url": "https://www.linkedin.com/in/john-doe"
}

patient_obj = Patient2(**patient)
insert(patient_obj)
