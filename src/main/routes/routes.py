from fastapi import APIRouter, Request
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.family_finder_composer import family_finder_composer
from src.main.composers.family_register_composer import family_register_composer
from src.main.composers.monthly_income_finder_composer import monthly_income_finder_composer
from src.main.composers.monthly_income_register_controller import monthly_income_register_composer
from src.main.composers.paid_bills_finder_composer import paid_bills_finder_composer
from src.main.composers.paid_bills_register_composer import paid_bills_register_composer
from src.errors.error_handler import handle_errors

router = APIRouter()

# Family Routes
@router.get('/family/find')
async def find_family(request: Request):
    http_response = None
    try:
        http_response = await request_adapter(request, family_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return http_response.body, http_response.status_code


@router.post('/family/')
async def register_family(request: Request):
    http_response = None
    try:
        http_response = await request_adapter(request, family_register_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return http_response.body, http_response.status_code

# MonthlyIncome Routes
@router.get('/monthlyincome/find')
async def find_income(request: Request):
    http_response = None
    try:
        http_response = await request_adapter(request, monthly_income_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return http_response.body, http_response.status_code

@router.post('/monthlyincome/')
async def register_income(request: Request):
    http_response = None
    try:
        http_response = await request_adapter(request, monthly_income_register_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return http_response.body, http_response.status_code

# PaidBills Routes
@router.get('/paidbills/find')
async def find_bills(request: Request):
    http_response = None
    try:
        http_response = await request_adapter(request, paid_bills_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return http_response.body, http_response.status_code

@router.post('/paidbills/')
async def register_bills(request: Request):
    http_response = None
    try:
        http_response = await request_adapter(request, paid_bills_register_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return http_response.body, http_response.status_code