from typing import List 
from src.domain.models.monthly_income import MonthlyIncome

class MonthlyIncomeSpy:
    def __init__(self) -> None:
        self.insert_monthly_income_attributes = {}
        self.select_monthly_income_attributes = {}
    
    def insert_monthly_income(self, family_id: int, income: float, date: str) -> None:
        self.insert_monthly_income_attributes["family_id"] = family_id
        self.insert_monthly_income_attributes["income"] = income
        self.insert_monthly_income_attributes["date"] = date
    
    def select_monthly_income(self, family_id: int) -> dict[MonthlyIncome]:
        self.select_monthly_income_attributes["family_id"] = family_id
        return [
            MonthlyIncome(1, family_id, 120, "12/02/2022"),
            MonthlyIncome(1, family_id, 500, "12/02/2022")
        ]
