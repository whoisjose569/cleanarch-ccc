from abc import ABC, abstractmethod
from typing import List
from src.domain.models.paid_bills import PaidBills

class PaidBillsRepositoryInterface(ABC):
    
    @abstractmethod
    def insert_paid_bills(self, family_id: int, type: str, value: float, payment_date: str) -> None: pass

    @abstractmethod
    def select_paid_bill_by_type(cls, type: str) -> List[PaidBills]: pass

    @abstractmethod
    def select_paid_bill_by_value(cls, value: float) -> List[PaidBills]: pass

    @abstractmethod
    def select_paid_bill_by_payment_date(cls, payment_date: str) -> List[PaidBills]: pass

    @abstractmethod
    def select_paid_bill_by_family_id(cls, family_id: int) -> PaidBills: pass
