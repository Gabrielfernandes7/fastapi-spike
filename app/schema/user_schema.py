from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str

class UserOutput(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
