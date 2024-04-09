import pytest
from .family_repository import FamilyRepository
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

def test_insert_family():
    mocked_family_name = 'teste'
    mocked_senha = 'teste'
    mocked_phone = 'teste'
    mocked_email = 'teste'
    
    family_repository = FamilyRepository()
    family_repository.insert_family(mocked_family_name, mocked_senha, mocked_phone, mocked_email)
    
    sql = '''
        SELECT * FROM family where family_name = '{}'
        AND senha = '{}'
        AND phone = '{}'
        AND email = '{}'
    '''.format(mocked_family_name, mocked_senha, mocked_phone, mocked_email)
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]
    
    assert registry.family_name == mocked_family_name
    assert registry.senha == mocked_senha
    assert registry.phone == mocked_phone
    assert registry.email == mocked_email
    
    connection.execute(text(f'''
                            DELETE FROM family WHERE id= {registry.id}'''))
    connection.commit()
    
def test_select_family():
    mocked_family_name = 'teste'
    mocked_senha = 'teste'
    mocked_phone = 'teste'
    mocked_email = 'teste'
    
    
    
    family_repository = FamilyRepository()
    family_repository.insert_family(mocked_family_name, mocked_senha, mocked_phone, mocked_email)
    response = family_repository.select_family(mocked_family_name)
    

    assert response[0].family_name == mocked_family_name
    assert response[0].senha == mocked_senha
    assert response[0].phone == mocked_phone
    assert response[0].email == mocked_email
    
    connection.execute(text(f'''
                            DELETE FROM family WHERE id = {response[0].id}'''))
    connection.commit()
    