from pydantic import BaseModel
from typing import Optional

class FamilySchema(BaseModel):
    family_name: str
    senha: str
    phone: str
    email: str
    
    class Config:
        orm_mode = True

