from abc import ABC, abstractmethod
from typing import Dict

class PaidBillsFinder(ABC):
    @abstractmethod
    def find_by_family_id(self, family_id: int) -> Dict: pass
