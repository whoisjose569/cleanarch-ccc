from typing import Dict
from src.domain.use_cases.monthly_income_register import MonthlyIncomeRegister as MonthlyIncomeRegisterInterface
from src.data.interfaces.monthly_income_repository import MonthlyIncomeRepository
from src.errors.types import HttpBadRequestError
class MonthlyIncomeRegister(MonthlyIncomeRegisterInterface):
    def __init__(self, monthly_income: MonthlyIncomeRepository) -> None:
        self.__monthly_income = monthly_income
    
    def register(self, family_id: int, income: float, date: str) -> Dict:
        self.__validate_income(income)
        self.registry_monthly_income_informations(family_id, income, date)
        
        response = self.__format_response(family_id, income, date)
        return response
    
    @classmethod
    def __validate_income(self, income: float):
        if income < 0:
            raise HttpBadRequestError('Valor negativo')
    
    
    def registry_monthly_income_informations(self, family_id: int, income: float, date: str):
        self.__monthly_income.insert_monthly_income(family_id, income, date)
    
    @classmethod
    def __format_response(cls, family_id, income, date) -> Dict:
        response = {
            "type": "MonthlyIncome",
            "count": 1,
            "attributes": {
                "family_id": family_id,
                "income": income,
                "date" : date
            }
        }
        return response