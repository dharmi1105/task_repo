import json
from pydantic import BaseModel, ValidationError, EmailStr
from datetime import datetime
class Employee(BaseModel):
    name : str
    Age : int
    email : EmailStr
    isactive : bool

with open('/Users/dpatibandla/Documents/training_files/JSON/employees.json','r') as file:
    json_data = json.load(file)


if __name__ == "__main__":

 if isinstance(json_data, list):
    for employee_data in json_data:
        try:
            employee = Employee(**employee_data)
            print("Validation Successful",employee)
        except ValidationError as e:
            print("Validation Failed",e)
 else:
    try:
        employee = Employee(**json_data)
        print("Validation Successful",employee)
    except ValidationError as e:
            print("Validation Failed",e)