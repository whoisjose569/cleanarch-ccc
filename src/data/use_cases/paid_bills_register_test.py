from src.infra.db.tests.paid_bills_repository import PaidBillsRepositorySpy
from .paid_bills_register import PaidBillsRegister

def test_register():
    family_id = 1
    type = "luz"
    value = 2000
    payment_date = '2000-05-02'
    
    repo = PaidBillsRepositorySpy()
    paid_bill_register = PaidBillsRegister(repo)
    
    response = paid_bill_register.register(family_id, type, value, payment_date)
    
    assert repo.insert_paid_bills_attributes['family_id'] == family_id
    assert repo.insert_paid_bills_attributes['type'] == type
    assert repo.insert_paid_bills_attributes['value'] == value
    assert repo.insert_paid_bills_attributes['payment_date'] == payment_date
    
    assert response["type"] == "PaidBills"
    assert response["count"] == 1
    assert response["attributes"]
