from typing import Dict
from src.domain.use_cases.family_register import FamilyRegister as FamilyRegisterInterface
from src.data.interfaces.family_repository import FamilyRepositoryInterface
from src.errors.types import HttpBadRequestError

class FamilyRegister(FamilyRegisterInterface):
    def __init__(self, family_repository: FamilyRepositoryInterface) -> None:
        self.__family_repository = family_repository
    
    def register(self, family_name: str, family_address: str, phone: str, email: str) -> Dict:
        self.__validate_name(family_name)
        self.__validate_email(email)
        self.__validate_phone(phone)
        
        self.__registry_family_informations(family_name, family_address, phone, email)
        response = self.__format_response(family_name, family_address, phone, email)
        return response
    
    @classmethod
    def __validate_name(cls, family_name: str) -> None:
        if len(family_name) > 30:
            raise HttpBadRequestError('Nome muito grande')
        
        if len(family_name) < 3:
            raise HttpBadRequestError('Nome muito pequeno')
    
    @classmethod
    def __validate_email(cls, email: str) -> None:
        if len(email) < 5:
            raise HttpBadRequestError('Email invalido')
        
    
    @classmethod
    def __validate_phone(cls, phone: str) -> None:
        if len(phone) < 6:
            raise HttpBadRequestError('Numero de telefone curto')
    
    def __registry_family_informations(self, family_name: str, family_address: str, phone: str, email: str) -> None:
        self.__family_repository.insert_family(family_name, family_address, phone, email)
    
    @classmethod
    def __format_response(cls, family_name, family_address, phone, email) -> Dict:
        response = {
            "type": "Family",
            "count": 1,
            "attributes": {
                "family_name": family_name,
                "family_address": family_address,
                "phone": phone,
                "email": email,
            }
        }
        return response