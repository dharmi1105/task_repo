import json
from pydantic import BaseModel, ValidationError, EmailStr, Field

#define employee model with aliases
class Employee(BaseModel):
    name : str = Field(alias = 'firstname')
    Age : int = Field(alias = 'Age of the user')
    email : EmailStr = Field(alias = 'email')
    isactive : bool = Field(alias = 'active_status')

#open and loas json file
with open('/Users/dpatibandla/Documents/training_files/JSON/employees.json','r') as file:
    json_data = json.load(file)

#empty list to store validated employee json objects
employee_list = []

if __name__ == "__main__":

 #validate json object and convert it to json object with aliases as keys
 if isinstance(json_data, list):
    for employee_data in json_data:
        try:
            employee = Employee(**employee_data)
            json_object = employee.dict(by_alias = True)
            employee_list.append(json_object)
            print("Validation Successful",employee)
        except ValidationError as e:
            print("Validation Failed",e)
 else:
    try:
        employee = Employee(**json_data)
        json_object = employee.dict(by_alias = True)
        employee_list.append(json_object)
        print("Validation Successful",employee)
    except ValidationError as e:
            print("Validation Failed",e)

print(('\n Json Object Data \n'),employee_list)