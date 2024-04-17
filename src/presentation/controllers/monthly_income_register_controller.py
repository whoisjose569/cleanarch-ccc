from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.monthly_income_register import MonthlyIncomeRegister as MonthlyIncomeRegisterInterface
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.schemas.monthly_income_schema import MonthlyIncomeSchema

class MonthlyIncomeRegisterController(ControllerInterface):
    def __init__(self, use_case: MonthlyIncomeRegisterInterface) -> None:
        self.__use_case = use_case
    
    def handle(self, monthly_income: MonthlyIncomeSchema)-> HttpResponse:
        try:
            family_id = monthly_income.family_id
            income = monthly_income.income
            date = monthly_income.date
            
            response = self.__use_case.register(family_id, income, date)
            
            return HttpResponse(
                status_code=200,
                body={"data": response}
            )
        except Exception as e:
            return HttpResponse(status_code=400, body=f'Error: {str(e)}')