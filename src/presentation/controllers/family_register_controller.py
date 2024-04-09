from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.family_register import FamilyRegister as FamilyRegisterInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class FamilyRegisterController(ControllerInterface):
    def __init__(self, use_case: FamilyRegisterInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            family_name = http_request.body['family_name']
            senha = http_request.body['senha']
            phone = http_request.body['phone']
            email = http_request.body['email']
            response = self.__use_case.register(family_name, senha, phone, email)
            return HttpResponse(
            status_code = 201,
            body={"data": response}
        )
        except:
            return HttpResponse(status_code=400, body={"error"})