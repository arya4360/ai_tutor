from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int]  # Make id optional
    name: str
    email: str
    address: str

    class Config:
        orm_mode = True

