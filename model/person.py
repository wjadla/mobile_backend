from typing import TypeVar, Optional
from pydantic import BaseModel

T = TypeVar('T')


class Person(BaseModel):
    id: str = None
    email: str
    password: str
    job: str
    role_name: str


class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T] = None
