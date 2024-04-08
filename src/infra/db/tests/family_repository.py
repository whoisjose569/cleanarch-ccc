from typing import List 
from src.domain.models.family import Family

class FamilyRepositorySpy:
    
    def __init__(self) -> None:
        self.insert_family_attributes = {}
        self.select_family_attributes = {}
    
    def insert_family(self, family_name: str, family_address: str, phone: str, email: str) -> None:
        self.insert_family_attributes["family_name"] = family_name
        self.insert_family_attributes["family_address"] = family_address
        self.insert_family_attributes["phone"] = phone
        self.insert_family_attributes["email"] = email
    
    def select_family(self, family_name: str) -> List[Family]:
        self.select_family_attributes["family_name"] = family_name
        return [
            Family(29, family_name, 'teste', 'teste', 'teste'),
            Family(29, family_name, 'teste_2', 'teste_2', 'teste_2')
        ]