from typing import Dict

class FamilyFinderSpy:
    def __init__(self) -> None:
        self.find_attributes = {}
    
    def find(self, family_name: str) -> Dict:
        self.find_attributes['family_name'] = family_name
        
        return {
            "type": "Family",
            "count": 1,
            "attributes": [
                {"family_name": family_name, "senha": "teste", "phone": "123", "email": "teste@email"}
            ]
        }