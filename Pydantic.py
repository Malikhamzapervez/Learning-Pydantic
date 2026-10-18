from pydantic import BaseModel, EmailStr,AnyUrl, Field # Field is used to add validation and metadata to model fields, AnyUrl is used to validate that a string is a valid URL, EmailStr is used to validate that a string is a valid email address
from typing import Annotated, List,Dict, Optional, Annotated # Optional is used to indicate that a field can be None

class Patient1(BaseModel):
   
    name: str
    age: int = Field(gt=0, description="Age must be a positive integer")     #Field is used to add validation and metadata to model fields, gt=0 means that the age must be greater than 0
    Height: Annotated[float, Field(gt=0, strict=True, description="Height must be a positive float")] = Field(default=None) #Field is used to add validation and metadata to model fields, gt=0 means that the height must be greater than 0, ans strict=True means that the height must be a float dont convert to int
    Weight: Annotated[float, Field(gt=0, strict=True, description="Weight must be a positive float")] = Field(default=None) #Field is used to add validation and metadata to model fields, gt=0 means that the weight must be greater than 0, ans strict=True means that the weight must be a float dont convert to int
    Linkedin_url: AnyUrl #AnyUrl is used to validate that a string is a valid URL
    married: Annotated[bool, Field(default=None)] = None
    allergies: Optional[list[str]] = None #Optional is used to indicate that a field can be None
    Contact: Dict[str, str]
    Email: EmailStr #EmailStr is used to validate that a string is a valid email address

def insert(patient: Patient1):

    if type(patient.name) is  str and type(patient.age) is  int:
        print(f"Name : {patient.name} and Age : {patient.age} are valid")
        print(f"Email is valid{patient.Email}")
        print(f"Contact is valid{patient.Contact}")
        print(f"Height is valid{patient.Height}")
        print(f"Weight is valid{patient.Weight}")
        print(f"Linkedin url is valid{patient.Linkedin_url}")
        
    else:
        raise TypeError("Age must be an integer")  

def Update(patient: Patient1):

    if type(patient.name) is  str and type(patient.age) is  int:
        print(f"Name : {patient.name} and Age : {patient.age} are updated")
    else:
        raise TypeError("Age must be an integer")  
    
patient = {"name": "John", "age": 25, "Height": 5.9, "Weight": 70.5,"Email": "john@example.com", "married": False, "allergies": ["pollen", "dust"], "Contact": { "phone": "123-456-7890"}, "Linkedin_url": "https://www.linkedin.com/in/john-doe"} 
patient_obj = Patient1(**patient)

insert(patient_obj)