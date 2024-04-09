from src.infra.db.repositories.monthly_income_repository import MonthlyIncomeRepository
from src.data.use_cases.monthly_income_register import MonthlyIncomeRegister
from src.presentation.controllers.monthly_income_register_controller import MonthlyIncomeRegisterController

def monthly_income_register_composer():
    repository = MonthlyIncomeRepository()
    use_case = MonthlyIncomeRegister(repository)
    controller = MonthlyIncomeRegisterController(use_case)
    
    return controller.handle