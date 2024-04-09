from typing import Callable
from fastapi import Request
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

async def request_adapter(request: Request, controller: Callable) -> HttpResponse:
    body = await request.json() if request.body else None

    http_request = HttpRequest(
        headers = request.headers,
        query_params=request.query_params,
        path_params=request.path_params,
        url=request.url,
        body=body
    )
    
    http_reponse = controller(http_request)
    
    return http_reponse