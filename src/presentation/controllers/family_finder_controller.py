from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.family_finder import FamilyFinder as FamilyFinderInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class FamilyFinderController(ControllerInterface):
    def __init__(self, use_case: FamilyFinderInterface) -> None:
        self.__use_case = use_case
        
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            family_name = http_request.query_params['family_name']
            
            response = self.__use_case.find(family_name)
            
            return HttpResponse(
                status_code=200,
                body={"data": response}
            )
        except:
            return HttpResponse(status_code=404, body={"error"})