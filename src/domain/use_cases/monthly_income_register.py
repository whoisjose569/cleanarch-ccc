from abc import ABC, abstractmethod
from typing import Dict


class MonthlyIncomeRegister(ABC):
    @abstractmethod
    def register(self, family_id: int, income: float, date: str) -> Dict: pass