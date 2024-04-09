from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.paid_bills_finder import PaidBillsFinder as PaidBillsFinderInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class PaidBillsFinderController(ControllerInterface):
    def __init__(self, use_case: PaidBillsFinderInterface) -> None:
        self.__use_case = use_case
        
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        family_id = http_request.query_params['family_id']
        
        response = self.__use_case.find_by_family_id(family_id)
        
        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
