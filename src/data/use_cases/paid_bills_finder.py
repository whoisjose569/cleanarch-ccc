from typing import Dict, List
from src.domain.use_cases.paid_bills_finder import PaidBillsFinder as PaidBillsFinderInterface
from src.data.interfaces.paid_bills_repository import PaidBillsRepositoryInterface
from src.domain.models.paid_bills import PaidBills

class PaidBillsFinder(PaidBillsFinderInterface):
    
    def __init__(self, paid_bills_repository: PaidBillsRepositoryInterface) -> None:
        self.__paid_bills_repository = paid_bills_repository
    
    def find_by_family_id(self, family_id: int) -> Dict:
        familys = self.__search_family(family_id)
        response = self.__format_response(familys)
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
