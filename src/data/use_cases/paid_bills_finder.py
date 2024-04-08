from typing import Dict, List
from src.domain.use_cases.paid_bills_finder import PaidBillsFinder as PaidBillsFinderInterface
from src.data.interfaces.paid_bills import PaidBillsRepository
from src.domain.models.paid_bills import PaidBills

class PaidBillsFinder(PaidBillsFinderInterface):
    
    def __init__(self, paid_bills_repository: PaidBillsRepository) -> None:
        self.__paid_bills_repository = paid_bills_repository
    
    def find_by_family_id(self, family_id: int) -> Dict:
        familys = self.__search_family(family_id)
        response = self.__format_response(familys)
        return response
    
    def find_by_payment_date(self, payment_date: str) -> Dict:
        dates = self.__search_payment_date(payment_date)
        response = self.__format_response(dates)
        return response
    
    def find_by_type(self, type: str) -> Dict:
        types = self.__search_type(type)
        response = self.__format_response(types)
        return response
    
    def find_by_value(self, value: float) -> Dict:
        values = self.__search_value(value)
        response = self.__format_response(values)
        return response

    @classmethod
    def __validate_value(cls, value: float):
        if value < 0:
            raise Exception('Valor negativo')
    

    def __search_family(self, family_id : int) -> List[PaidBills]:
        family_search = self.__paid_bills_repository.select_paid_bill_by_family_id(family_id)
        if family_search == []:
            raise Exception('Familia não encontrada')
        return family_search
    
    def __search_type(self, type: str) -> List[PaidBills]:
        type_search = self.__paid_bills_repository.select_paid_bill_by_type(type)
        if type_search == []:
            raise Exception('Tipo de conta não encontrada')
        return type_search

    def __search_value(self, value: float) -> List[PaidBills]:
        value_search = self.__paid_bills_repository.select_paid_bill_by_value(value)
        if value_search == []:
            raise Exception('Conta não encontrada')
        return value_search

    def __search_payment_date(self, payment_date: str) -> List[PaidBills]:
        payment_date_search = self.__paid_bills_repository.select_paid_bill_by_payment_date(payment_date)
        if payment_date_search == []:
            raise Exception('Conta não encontrada')
        return payment_date_search
    
    def __format_response(cls, bills: List[PaidBills]) -> Dict:
        attributes = []
        for bill in bills:
            attributes.append(
                {"family_id": bill.family_id, "type": bill.type, "value": bill.value, "payment_date": bill.payment_date}
            )
        response = {
            "type": "PaidBills",
            "count": len(bills),
            "attributes": attributes
        }
        return response