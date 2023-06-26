import string

import pydantic


class Algorithms_validator(pydantic.BaseModel):
    complexity: str
    name: str
    mathematical_ecuation: str
    description: str

    @pydantic.validator("name")
    @classmethod
    def name_validator(cls, value):
        if any(p in value for p in string.punctuation):
            raise ValueError("cannot include puntuation")
        if any(d in value for d in string.digits):
            raise ValueError("cannot include digits")
        else:
            return value
