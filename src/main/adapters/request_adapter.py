from typing import Callable
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.schemas.family_schema import FamilySchema

async def request_adapter(request, controller: Callable) -> HttpResponse:
    http_response = controller(request)
    
    return http_response