from typing import Dict

class FamilyRegisterSpy:
    def __init__(self) -> None:
        self.register_attributes = {}
    
    def register(self, family_name: str, senha: str, phone: str, email: str) -> Dict:
        self.register_attributes['family_name'] = family_name
        self.register_attributes['senha'] = senha
        self.register_attributes['phone'] = phone
        self.register_attributes['email'] = email
        
        return{
            "type" : "Family",
            "count": 1,
            "attributes": [
                {"family_name": family_name,
                "senha": senha,
                "phone": phone,
                "email": email}
            ]
        }