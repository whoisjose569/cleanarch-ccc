from .family_repository import FamilyRepository

def test_insert_family():
    mocked_family_name = 'teste'
    mocked_family_address = 'teste'
    mocked_phone = 'teste'
    mocked_email = 'teste'
    
    family_repository = FamilyRepository()
    family_repository.insert_family(mocked_family_name, mocked_family_address, mocked_phone, mocked_email)