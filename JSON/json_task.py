import json
import pandas as pd
from pydantic import BaseModel, ValidationError, EmailStr
class Employee(BaseModel):
    name : str
    Age : int
    email : EmailStr
    department : str
    isactive : bool

if __name__ == "__main__":

    # import data from file in data object

    df = pd.read_json('employees.json')
    print (df.to_string())

    #for record in data:
        #try:
            #employee = Employee(**data)
            #print(f"Valid employee record: {employee.name}")
        #except ValidationError as e:
          # print(f"Invalid employee record: {record['name']}")
           # print(f"Errors: {e.errors()}")
