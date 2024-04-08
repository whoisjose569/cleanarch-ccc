from src.infra.db.tests.family_repository import FamilyRepositorySpy
from.family_register import FamilyRegister

def test_register():
    family_name = 'teste'
    family_address = 'teste'
    phone = "40028922"
    email = "teste@email"
    
    repo = FamilyRepositorySpy()
    family_register = FamilyRegister(repo)
    
    response = family_register.register(family_name, family_address, phone, email)
    
    assert repo.insert_family_attributes["family_name"] == family_name
    assert repo.insert_family_attributes["family_address"] == family_address
    assert repo.insert_family_attributes["phone"] == phone
    assert repo.insert_family_attributes['email'] == email
    
    assert response["type"] == "Family"
    assert response["count"] == 1
    assert response["attributes"]

def test_register_family_name_error():
    family_name = 'teste123'
    family_address = 'teste'
    phone = '40028922'
    email = 'teste@email'
    
    repo = FamilyRepositorySpy()
    family_register = FamilyRegister(repo)
    
    try:
        family_register.register(family_name, family_address, phone, email)
    except Exception as exception:
        assert str(exception) == "Nome invalido"

def test_register_family_name_to_long():
    family_name = 'testetestetestetestestestesteste'
    family_address = 'teste'
    phone = '40028922'
    email = 'teste@email'
    
    repo = FamilyRepositorySpy()
    family_register = FamilyRegister(repo)
    
    try:
        family_register.register(family_name, family_address, phone, email)
    except Exception as exception:
        assert str(exception) == "Nome muito grande"

def test_register_family_name_to_short():
    family_name = 'tes'
    family_address = 'teste'
    phone = '40028922'
    email = 'teste@email'
    
    repo = FamilyRepositorySpy()
    family_register = FamilyRegister(repo)
    
    try:
        family_register.register(family_name, family_address, phone, email)
    except Exception as exception:
        assert str(exception) == "Nome muito pequeno"

def test_register_family_email_to_short():
    family_name = 'teste'
    family_address = 'teste'
    phone = '40028922'
    email = 'tes'
    
    repo = FamilyRepositorySpy()
    family_register = FamilyRegister(repo)
    
    try:
        family_register.register(family_name, family_address, phone, email)
    except Exception as exception:
        assert str(exception) == "Email invalido"

def test_register_family_phone_to_short():
    family_name = 'teste'
    family_address = 'teste'
    phone = '4002'
    email = 'teste@email'
    
    repo = FamilyRepositorySpy()
    family_register = FamilyRegister(repo)
    
    try:
        family_register.register(family_name, family_address, phone, email)
    except Exception as exception:
        assert str(exception) == "Numero de telefone curto"