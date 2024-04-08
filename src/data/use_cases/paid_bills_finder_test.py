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

def test_find_value():
    value = 200
    
    repo = PaidBillsRepositorySpy()
    paid_bills_finder = PaidBillsFinder(repo)
    
    response = paid_bills_finder.find_by_value(value)
    
    assert response["type"] == "PaidBills"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]

def test_find_date():
    date = "2000-05-21"
    
    repo = PaidBillsRepositorySpy()
    paid_bills_finder = PaidBillsFinder(repo)
    
    response = paid_bills_finder.find_by_payment_date(date)
    
    assert response["type"] == "PaidBills"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]

def test_find_type():
    type = "Luz"
    
    repo = PaidBillsRepositorySpy()
    paid_bills_finder = PaidBillsFinder(repo)
    
    response = paid_bills_finder.find_by_type(type)
    
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

def test_find_error_type():
    class PaidBillsERROR(PaidBillsRepositorySpy):
        def select_paid_bill_by_type(self, type: str):
            return []

    type = "agua"
    
    repo = PaidBillsERROR()
    paid_bills_finder = PaidBillsFinder(repo)
    
    try:
        paid_bills_finder.find_by_type(type)
        assert False
    except Exception as exception:
        assert str(exception) == ('Tipo de conta não encontrada')

def test_find_error_date():
    class PaidBillsERROR(PaidBillsRepositorySpy):
        def select_paid_bill_by_payment_date(self, payment_date: str):
            return []

    date = "1"
    
    repo = PaidBillsERROR()
    paid_bills_finder = PaidBillsFinder(repo)
    
    try:
        paid_bills_finder.find_by_payment_date(date)
        assert False
    except Exception as exception:
        assert str(exception) == ('Conta não encontrada')


