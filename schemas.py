from typing import List
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(min_length=3)
    password: str = Field(min_length=3)
    phone_number: str
    class Config:
        json_schema_extra = {
            "example": {
                "username": "Enter Username",
                "password": "Enter Password",
                "phone_number": "Enter Phone Number"
            }
        }