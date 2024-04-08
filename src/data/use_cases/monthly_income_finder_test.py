from src.domain.models.monthly_income import MonthlyIncome
from src.infra.db.tests.monthly_income_repository import MonthlyIncomeSpy
from .monthly_income_finder import MonthlyIncomeFinder

def test_find():
    family_id = 1
    
    repo = MonthlyIncomeSpy()
    income_repository = MonthlyIncomeFinder(repo)
    
    response = income_repository.find(family_id)
    
    assert response["type"] == "MonthlyIncome"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]

def test_find_error_income_not_found():
    class MonthlyIncomeRepositoryERROR(MonthlyIncomeSpy):
        def select_monthly_income(self, family_id: int):
            return []
    
    family_id = 1
    
    repo = MonthlyIncomeRepositoryERROR()
    income_repository = MonthlyIncomeFinder(repo)
    try:
        income_repository.find(family_id)
        assert False
    except Exception as expection:
        assert str(expection) == "Renda não encontrada"