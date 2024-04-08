import pytest
from .family_repository import FamilyRepository
from .monthly_income_repository import MonthlyIncomeRepository
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

def test_insert_monthly_income():
    mocked_family_name = 'teste'
    mocked_family_address = 'teste'
    mocked_phone = 'teste'
    mocked_email = 'teste'
    
    family_repository = FamilyRepository()
    family_repository.insert_family(mocked_family_name, mocked_family_address, mocked_phone, mocked_email)
    
    mocked_family_id = 29
    mocked_income = 120
    mocked_date = "12/07/2023"
    
    monthly_income_repository = MonthlyIncomeRepository()
    monthly_income_repository.insert_monthly_income(mocked_family_id, mocked_income, mocked_date)
    
    sql = '''
        SELECT * FROM monthly_income where family_id = '{}'
        AND income = '{}'
        AND date = '{}'
    '''.format(mocked_family_id, mocked_income, mocked_date)
    
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]
    
    assert registry.family_id == mocked_family_id
    assert registry.income == mocked_income
    assert registry.date == mocked_date
    
    connection.execute(text(f'''
                            DELETE FROM family where id = {mocked_family_id}
                            '''))
    connection.execute(text(f'''
                            DELETE FROM monthly_income where family_id = {registry.family_id}'''))
    connection.commit()
