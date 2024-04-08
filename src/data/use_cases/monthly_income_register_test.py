from src.infra.db.tests.monthly_income_repository import MonthlyIncomeSpy
from .monthly_income_register import MonthlyIncomeRegister

def test_register():
    family_id = 1
    income = 200
    date = "2000-07-21"
    
    repo = MonthlyIncomeSpy()
    month_income_repository = MonthlyIncomeRegister(repo)
    
    response = month_income_repository.register(family_id, income, date)
    
    
    assert repo.insert_monthly_income_attributes["family_id"] == family_id
    assert repo.insert_monthly_income_attributes["income"] == income
    assert repo.insert_monthly_income_attributes["date"] == date
    
    assert response["type"] == "MonthlyIncome"
    assert response["count"] == 1
    assert response["attributes"]

def test_register_income_error():
    family_id = 1
    income = -50
    date = "2000-07-21"
    
    repo = MonthlyIncomeSpy()
    month_income_repository = MonthlyIncomeRegister(repo)
    
    try:
        month_income_repository.register(family_id, income, date)
    except Exception as exception:
        assert str(exception) == "Valor negativo"