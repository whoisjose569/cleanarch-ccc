from abc import ABC, abstractmethod
from typing import Dict

class PaidBillsRegister(ABC):
    
    @abstractmethod
    def register(self, family_id: int, type: str, value: float, payment_date: str) -> Dict: pass