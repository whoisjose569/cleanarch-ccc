from abc import ABC, abstractmethod
from typing import List
from src.domain.models.monthly_income import MonthlyIncome

class MonthlyIncomeRepository(ABC):

    @abstractmethod
    def insert_monthly_income(self, family_id: int, income: float, date: str) -> None: pass
    
    @abstractmethod
    def select_monthly_income(self, family_id: int) ->List[MonthlyIncome]: pass