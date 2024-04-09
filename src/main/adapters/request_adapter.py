from typing import Callable
from fastapi import Request
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

async def request_adapter(request: Request, controller: Callable) -> HttpResponse:
    body = await request.json() if request.method != "GET" and request.body else None

    http_request = HttpRequest()
    http_request.headers = request.headers
    http_request.query_params = request.query_params
    http_request.path_params = request.path_params
    http_request.url = request.url
    http_request.body = body
    
    http_response = controller(http_request)
    
    return http_response