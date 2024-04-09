from typing import List
from src.domain.models.paid_bills import PaidBills
from src.infra.db.tests.paid_bills_repository import PaidBillsRepositorySpy
from .paid_bills_finder import PaidBillsFinder

def test_find_id():
    family_id = 1
    
    repo = PaidBillsRepositorySpy()
    paid_bills_finder = PaidBillsFinder(repo)
    
    response = paid_bills_finder.find_by_family_id(family_id)
    
    assert response["type"] == "PaidBills"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]

def test_negative_value():
    value = 200
    
    repo = PaidBillsRepositorySpy()
    paid_bills_finder = PaidBillsFinder(repo)
    
    try:
        paid_bills_finder.find_by_value(value)
    except Exception as exception:
        assert str(exception) == 'Valor negativo'

def test_find_error_family():
    class PaidBillsERROR(PaidBillsRepositorySpy):
        def select_paid_bill_by_family_id(self, family_id: int):
            return []

    family_id = 999
    
    repo = PaidBillsERROR()
    paid_bills_finder = PaidBillsFinder(repo)
    
    try:
        paid_bills_finder.find_by_family_id(family_id)
        assert False
    except Exception as exception:
        assert str(exception) == ('Familia não encontrada')
