from src.infra.db.repositories.monthly_income_repository import MonthlyIncomeRepository
from src.data.use_cases.monthly_income_finder import MonthlyIncomeFinder
from src.presentation.controllers.monthly_income_finder_controller import MonthlyIncomeFinderController

def monthly_income_finder_composer():
    repository = MonthlyIncomeRepository()
    use_case = MonthlyIncomeFinder(repository)
    controller = MonthlyIncomeFinderController(use_case)
    
    return controller.handle