from abc import ABC, abstractmethod
from typing import Dict

class PaidBillsFinder(ABC):
    @abstractmethod
    def find_by_type(self, type: str) -> Dict: pass
    
    @abstractmethod
    def find_by_value(self, value: float) -> Dict: pass
    
    @abstractmethod
    def find_by_payment_date(self, payment_date: str) -> Dict: pass
    
    @abstractmethod
    def find_by_family_id(self, family_id: int) -> Dict: pass
