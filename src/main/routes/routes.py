from fastapi import APIRouter, Request
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.family_finder_composer import family_finder_composer
from src.main.composers.family_register_composer import family_register_composer

router = APIRouter()

@router.get('/family/find')
async def find_family(request: Request):
    http_response = None
    try:
        http_response = await request_adapter(request, family_finder_composer())
    except Exception as exception:
        raise exception
    return http_response

@router.post('/family/')
async def register_family(request: Request):
    http_response = None
    try:
        http_response = await request_adapter(request, family_register_composer())
    except Exception as exception:
        raise exception
    return http_response