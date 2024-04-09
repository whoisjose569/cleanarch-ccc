from typing import Dict, List
from src.domain.use_cases.family_finder import FamilyFinder as FamilyFinderInterface
from src.data.interfaces.family_repository import FamilyRepositoryInterface
from src.domain.models.family import Family
from src.errors.types import HttpNotFoundError, HttpBadRequestError

class FamilyFinder(FamilyFinderInterface):
    def __init__(self, family_repository: FamilyRepositoryInterface) -> None:
        self.__family_repository = family_repository
    
    def find(self, family_name: str) -> Dict:
        self.__validate_name(family_name)
        familys = self.__search_family(family_name)
        response = self.__format_response(familys)
        return response
    
    @classmethod
    def __validate_name(cls, family_name: str) -> None:
        if not family_name.isalpha():
            raise HttpBadRequestError('Nome Invalido')
        
        if len(family_name) > 15:
            raise HttpBadRequestError('Nome muito grande')
        
        if len(family_name) < 4:
            raise HttpBadRequestError('Nome muito pequeno')
    

    def __search_family(self, family_name: str) -> List[Family]:
        family = self.__family_repository.select_family(family_name)
        if family == []:
            raise HttpNotFoundError('Familia não encontrada')
        return family

    @classmethod
    def __format_response(cls, familys: List[Family]) -> Dict:
        attributes = []
        for family in familys:
            attributes.append(
                {"family_name": family.family_name, "family_address": family.family_address, "phone": family.phone, "email": family.email}
            )
        reponse = {
            "type": "Family",
            "count": len(familys),
            "attributes": attributes
        }
        return reponse