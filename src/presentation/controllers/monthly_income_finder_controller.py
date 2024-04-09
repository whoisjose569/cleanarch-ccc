from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.monthly_income_finder import MonthlyIncomeFinder
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class MonthlyIncomeFinderController(ControllerInterface):
    def __init__(self, use_case: MonthlyIncomeFinder) -> None:
        self.__use_case = use_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        family_id = http_request.query_params['family_id']
        
        response = self.__use_case.find(family_id)
        
        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
