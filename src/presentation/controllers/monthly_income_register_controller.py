from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.monthly_income_register import MonthlyIncomeRegister as MonthlyIncomeRegisterInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class MonthlyIncomeRegisterController(ControllerInterface):
    def __init__(self, use_case: MonthlyIncomeRegisterInterface) -> None:
        self.__use_case = use_case
    
    def handle(self, http_request: HttpRequest)-> HttpResponse:
        family_id = http_request.body['family_id']
        income = http_request.body['income']
        date = http_request.body['date']
        
        response = self.__use_case.register(family_id, income, date)
        
        return HttpResponse(
            status_code=200,
            body={"data": response}
        )