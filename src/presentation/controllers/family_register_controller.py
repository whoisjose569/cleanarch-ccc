from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.family_register import FamilyRegister as FamilyRegisterInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.schemas.family_schema import FamilySchema

class FamilyRegisterController(ControllerInterface):
    def __init__(self, use_case: FamilyRegisterInterface) -> None:
        self.__use_case = use_case

    def handle(self, family: FamilySchema) -> HttpResponse:
        try:
            family_name = family.family_name
            senha = family.senha
            phone = family.phone
            email = family.email
            response = self.__use_case.register(family_name, senha, phone, email)
            return HttpResponse(
            status_code = 201,
            body={"data": response}
        )
        except Exception as e:
            return HttpResponse(status_code=400, body=f'Error: {str(e)}')