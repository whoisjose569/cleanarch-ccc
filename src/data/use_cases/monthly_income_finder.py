from typing import Dict, List
from src.domain.use_cases.monthly_income_finder import MonthlyIncomeFinder as MonthlyIncomeFinderInterface
from src.data.interfaces.monthly_income_repository import MonthlyIncomeRepository
from src.domain.models.monthly_income import MonthlyIncome
from src.errors.types import HttpNotFoundError

class MonthlyIncomeFinder(MonthlyIncomeFinderInterface):
    def __init__(self, monthly_income_repository: MonthlyIncomeRepository) -> None:
        self.__monthly_income_repository = monthly_income_repository
    
    def find(self, family_id: int) -> Dict:
        incomes = self.__search_monthly_income(family_id)
        response = self.__format_response(incomes)
        return response
    
    def __search_monthly_income(self, family_id: int) -> List[MonthlyIncome]:
        monthly_income = self.__monthly_income_repository.select_monthly_income(family_id)
        if monthly_income == []:
            raise HttpNotFoundError('Renda não encontrada')
        return monthly_income

    @classmethod
    def __format_response(cls, incomes: List[MonthlyIncome]) -> Dict:
        attributes = []
        for income in incomes:
            attributes.append(
                {"family_id": income.family_id, "income": income.income, "date": income.date}
            )
        response = {
            "type": "MonthlyIncome",
            "count": len(incomes),
            "attributes": attributes
        }
        return response