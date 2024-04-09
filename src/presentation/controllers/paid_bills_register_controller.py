from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.paid_bills_register import PaidBillsRegister as PaidBillsRegisterInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class PaidBillsRegisterController(ControllerInterface):
    def __init__(self, use_case: PaidBillsRegisterInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        family_id = http_request.body['family_id']
        type = http_request.body['type']
        value = http_request.body['value']
        payment_date = http_request.body['payment_date']
        response = self.__use_case.register(family_id, type, value, payment_date)
        
        return HttpResponse(
            status_code = 200,
            body={"data": response}
        )