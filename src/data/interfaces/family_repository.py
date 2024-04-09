from abc import ABC, abstractmethod
from typing import List
from src.domain.models.family import Family

class FamilyRepositoryInterface(ABC):
    
    @abstractmethod
    def insert_family(self, family_name: str, senha: str, phone: str, email: str) -> None: pass
    
    @abstractmethod
    def select_family(self, family_name: str) -> List[Family]: pass