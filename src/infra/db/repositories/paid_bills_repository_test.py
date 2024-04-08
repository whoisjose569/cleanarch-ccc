import pytest
from .family_repository import FamilyRepository
from .paid_bills_repository import PaidBillsRepository
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

def test_insert_paid_bills():
    mocked_family_name = 'teste'
    mocked_family_address = 'teste'
    mocked_phone = 'teste'
    mocked_email = 'teste'
    
    family_repository = FamilyRepository()
    family_repository.insert_family(mocked_family_name, mocked_family_address, mocked_phone, mocked_email)
    
    mocked_family_id = 29
    mocked_type = "Luz"
    mocked_value= 120
    mocked_payment_date = "12/07/2000"
    
    paid_bills_repository = PaidBillsRepository()
    paid_bills_repository.insert_paid_bills(mocked_family_id, mocked_type, mocked_value, mocked_payment_date)
    
    sql = '''
        SELECT * FROM paid_bills where family_id = '{}'
        AND type = '{}'
        AND value = '{}'
        AND payment_date = '{}'
    '''.format(mocked_family_id, mocked_type, mocked_value, mocked_payment_date)
    
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]
    
    assert registry.family_id == mocked_family_id
    assert registry.type == mocked_type
    assert registry.value == mocked_value
    assert registry.payment_date == mocked_payment_date

def test_select_paid_bill_by_type():
    mocked_family_name = 'teste'
    mocked_family_address = 'teste'
    mocked_phone = 'teste'
    mocked_email = 'teste'
    
    family_repository = FamilyRepository()
    family_repository.insert_family(mocked_family_name, mocked_family_address, mocked_phone, mocked_email)
    
    mocked_family_id = 29
    mocked_type = "Luz"
    mocked_value= 120
    mocked_payment_date = "12/07/2000"
    
    paid_bills_repository = PaidBillsRepository()
    paid_bills_repository.insert_paid_bills(mocked_family_id, mocked_type, mocked_value, mocked_payment_date)
    
    response = paid_bills_repository.select_paid_bill_by_type(mocked_type)
    
    assert response[0].type == mocked_type

def test_select_paid_bill_by_value():
    mocked_family_name = 'teste'
    mocked_family_address = 'teste'
    mocked_phone = 'teste'
    mocked_email = 'teste'
    
    family_repository = FamilyRepository()
    family_repository.insert_family(mocked_family_name, mocked_family_address, mocked_phone, mocked_email)
    
    mocked_family_id = 29
    mocked_type = "Luz"
    mocked_value= 120
    mocked_payment_date = "12/07/2000"
    
    paid_bills_repository = PaidBillsRepository()
    paid_bills_repository.insert_paid_bills(mocked_family_id, mocked_type, mocked_value, mocked_payment_date)
    
    response = paid_bills_repository.select_paid_bill_by_value(mocked_value)
    
    assert response[0].value == mocked_value