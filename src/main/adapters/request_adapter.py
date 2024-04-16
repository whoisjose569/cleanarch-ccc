from typing import Callable
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.schemas.family_schema import FamilySchema

async def request_adapter(family: FamilySchema, controller: Callable) -> HttpResponse:
    schema_dict = {"family_name": family.family_name, "senha": family.senha, "phone": family.phone, "email": family.email}
    http_response = controller(schema_dict)
    
    return http_response