from abc import ABC, abstractmethod
from typing import Dict

class FamilyRegister(ABC):
    
    @abstractmethod
    def register(self, family_name: str, senha: str, phone: str, email: str) -> Dict: pass