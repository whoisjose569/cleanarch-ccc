from abc import ABC, abstractmethod
from typing import Dict


class MonthlyIncomeFinder(ABC):
    @abstractmethod
    def find(self, family_id: int) -> Dict: pass