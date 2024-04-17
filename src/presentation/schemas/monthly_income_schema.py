from pydantic import BaseModel
from typing import Optional

class MonthlyIncomeSchema(BaseModel):
    family_id: int
    income: float
    date: str
    
    class Config:
        orm_mode = True