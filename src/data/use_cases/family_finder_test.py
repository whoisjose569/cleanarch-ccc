from src.infra.db.tests.family_repository import FamilyRepositorySpy
from .family_finder import FamilyFinder

def test_find():
    family_name = 'teste'

    repo = FamilyRepositorySpy()
    family_finder = FamilyFinder(repo)

    response = family_finder.find(family_name)
    
    assert response["type"] == "Family"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]

def test_find_error_in_valid_name():
    family_name = 'teste'
    
    repo= FamilyRepositorySpy()
    family_finder = FamilyFinder(repo)
    
    try:
        family_finder.find(family_name)
    except Exception as exception:
        assert str(exception) == 'Nome Invalido'

def test_find_error_in_long_name():
    family_name = 'testetestestestestestestestestestestestes'
    
    repo= FamilyRepositorySpy()
    family_finder = FamilyFinder(repo)

    try:
        family_finder.find(family_name)
    except Exception as exception:
        assert str(exception) == 'Nome muito grande'

def test_find_error_in_short_name():
    family_name = 'tes'
    
    repo= FamilyRepositorySpy()
    family_finder = FamilyFinder(repo)

    try:
        family_finder.find(family_name)
    except Exception as exception:
        assert str(exception) == 'Nome muito pequeno'

def test_find_error_family_not_found():
    class FamilyRepositoryError(FamilyRepositorySpy):
        def select_family(self, family_name: str):
            return []
    
    family_name = 'teste'
    
    repo = FamilyRepositoryError()
    family_finder = FamilyFinder(repo)
    
    try:
        family_finder.find(family_name)
        assert False
    except Exception as expection:
        assert str(expection) == "Familia não encontrada"
