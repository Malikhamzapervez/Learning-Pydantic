from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    pin_code: str

class new_patient(BaseModel):
    name: str
    age: int
    gender : str
    address: Address

address_data = {
    "street": "123 Main St",
    "city": "Anytown",
    "pin_code": "12345"
}

address1 = Address(**address_data)

patient_data = {
    "name": "John Doe",
    "age": 30,
    "gender": "Male",
    "address": address1

}
 
patient_obj = new_patient(**patient_data)

print(patient_obj.address.street)  # Output: 123 Main St
print(patient_obj.address.city)    # Output: Anytown
print(patient_obj.address.pin_code) # Output: 12345