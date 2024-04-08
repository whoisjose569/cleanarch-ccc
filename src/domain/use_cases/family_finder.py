from abc import ABC, abstractmethod
from typing import Dict

class FamilyFinder(ABC):
    @abstractmethod
    def find(self, family_name: str) -> Dict: pass