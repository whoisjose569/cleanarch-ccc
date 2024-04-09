from typing import List
from src.domain.models.paid_bills import PaidBills

class PaidBillsRepositorySpy():
    def __init__(self) -> None:
        self.insert_paid_bills_attributes = {}
        self.__select_paid_bills_attributes = {}

    def insert_paid_bills(self, family_id: int, type: str, value: float, payment_date: str) -> None:
        self.insert_paid_bills_attributes["family_id"] = family_id
        self.insert_paid_bills_attributes["type"] = type
        self.insert_paid_bills_attributes["value"] = value
        self.insert_paid_bills_attributes["payment_date"] = payment_date
    
    def select_paid_bill_by_type(self, type: str) -> List[PaidBills]: 
        self.__select_paid_bills_attributes["type"] = type
        return [
            PaidBills(1,1,type,200,"2000-05-21"),
            PaidBills(1,1,type,2000,"2000-05-21")
        ]
    
    def select_paid_bill_by_value(self, value: int) -> List[PaidBills]: 
        self.__select_paid_bills_attributes["value"] = value
        return [
            PaidBills(1,1,"luz",value,"2000-05-21"),
            PaidBills(1,1,"luz",value,"2000-05-21")
        ]
    
    def select_paid_bill_by_payment_date(self, payment_date: str) -> List[PaidBills]: 
        self.__select_paid_bills_attributes["payment_date"] = payment_date
        return [
            PaidBills(1,1,"luz",200,payment_date),
            PaidBills(1,1,"luz",2000,payment_date)
        ]
    def select_paid_bill_by_family_id(self, family_id: int) -> List[PaidBills]:
        self.__select_paid_bills_attributes["family_id"] = family_id
        return [
            PaidBills(1,family_id,"luz",200,"2000-05-21")
        ]