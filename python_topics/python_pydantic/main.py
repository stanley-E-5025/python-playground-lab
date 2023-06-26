import logging
from typing import List

from pydantic import BaseModel, validator

logging.basicConfig(level=logging.INFO)

class User(BaseModel):
    name: str
    age: int
    email: str
    password: str
    roles: List[str]
    
    @validator("password", pre=True)
    def check_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not any(c.isupper() for c in value):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not any(c.isdigit() for c in value):
            raise ValueError("Password must contain at least one digit.")
        return value
    
    @validator("email")
    def check_email(cls, value):
        if '@' not in value:
            raise ValueError("Invalid email format.")
        return value
    
    @validator("age")
    def check_age(cls, value):
        if value < 18:
            raise ValueError("Age must be 18 or older.")
        return value



try:
    user = User(name="John Smith", age=20, email="john.smith@example.com", password="Pa$$w0rd", roles=["admin"])
    logging.info(f'valid user: {user}')
except ValueError as e:
    logging.error(f'Invalid user: {e}')

