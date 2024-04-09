from typing import Dict
from src.domain.use_cases.paid_bills_register import PaidBillsRegister as PaidBillsRegisterInterface
from src.data.interfaces.paid_bills_repository import PaidBillsRepositoryInterface

class PaidBillsRegister(PaidBillsRegisterInterface):
    def __init__(self, paid_bills_repository: PaidBillsRepositoryInterface) -> None:
        self.__paid_bills_repository = paid_bills_repository
    
    def register(self, family_id: int, type: str, value: float, payment_date: str) -> Dict:
        self.__validate_value(value)
        self.__register_paid_bills_information(family_id, type, value, payment_date)
        response = self.__format_response(family_id, type, value, payment_date)
        return response

    def __register_paid_bills_information(self, family_id: int, type: str, value: float, payment_date: str):
        self.__paid_bills_repository.insert_paid_bills(family_id, type, value, payment_date)


    def __validate_value(cls, value: float):
        if value < 0:
            raise Exception('Valor negativo')

    @classmethod
    def __format_response(cls, family_id, type, value, payment_date) -> Dict:
        response = {
            "type": "PaidBills",
            "count": 1,
            "attributes": {
                "family_id": family_id,
                "type": type,
                "value": value,
                "payment_date": payment_date,
            }
        }
        return response