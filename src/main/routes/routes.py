from fastapi import APIRouter, Request, HTTPException, Depends
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.family_finder_composer import family_finder_composer
from src.main.composers.family_register_composer import family_register_composer
from src.main.composers.monthly_income_finder_composer import monthly_income_finder_composer
from src.main.composers.monthly_income_register_controller import monthly_income_register_composer
from src.main.composers.paid_bills_finder_composer import paid_bills_finder_composer
from src.main.composers.paid_bills_register_composer import paid_bills_register_composer
from src.errors.error_handler import handle_errors
from fastapi.security import OAuth2PasswordBearer
from src.data.use_cases.family_finder import FamilyFinder
from src.infra.db.repositories.family_repository import FamilyRepository
import json
from src.domain.providers.token_provider import verify_access_token
from src.domain.providers.token_provider import create_access_token
from src.domain.providers.hash_provider import verify_hash
from src.presentation.schemas.family_schema import FamilySchema

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

# Family Routes
@router.get('/family/find', dependencies=[Depends(verify_access_token)])
async def find_family(request: Request):
    try:
        http_response = await request_adapter(request, family_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return http_response.body, http_response.status_code


@router.post('/family/')
async def register_family(family: FamilySchema):
    http_response = None
    try:
        http_response = await request_adapter(family, family_register_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return http_response.body, http_response.status_code

# MonthlyIncome Routes
@router.get('/monthlyincome/find', dependencies=[Depends(verify_access_token)])
async def find_income(request: Request):
    http_response = None
    try:
        http_response = await request_adapter(request, monthly_income_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return http_response.body, http_response.status_code

@router.post('/monthlyincome/', dependencies=[Depends(verify_access_token)])
async def register_income(request: Request):
    http_response = None
    try:
        http_response = await request_adapter(request, monthly_income_register_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return http_response.body, http_response.status_code

# PaidBills Routes
@router.get('/paidbills/find', dependencies=[Depends(verify_access_token)])
async def find_bills(request: Request):
    http_response = None
    try:
        http_response = await request_adapter(request, paid_bills_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return http_response.body, http_response.status_code


@router.post('/paidbills/', dependencies=[Depends(verify_access_token)])
async def register_bills(request: Request):
    http_response = None
    try:
        http_response = await request_adapter(request, paid_bills_register_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return http_response.body, http_response.status_code

@router.post("/token")
async def generate_token(request: Request):
    try:
        dados = await request.body()
        data = json.loads(dados.decode('utf-8'))
        email = data['email']
        senha = data['senha']

        repository = FamilyRepository
        localized_family = FamilyFinder(repository).find(email)

        valid_email = localized_family['attributes'][0]['email']
        if valid_email != email:
            return HTTPException(status_code=400, detail="email invalid")

        valid_password = verify_hash(senha, localized_family['attributes'][0]['senha'])

        if not valid_password:
            return HTTPException(status_code=400, detail="senha invalid")
        dict = {
            "email": email,
            "password": senha
        }
        access_token = create_access_token(dict)
        return access_token
    except Exception as exception:
        http_response = handle_errors(exception)
    return http_response.body, http_response.status_code
