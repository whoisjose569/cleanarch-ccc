from typing import Dict

class FamilyRegisterSpy:
    def __init__(self) -> None:
        self.register_attributes = {}
    
    def register(self, family_name: str, family_address: str, phone: str, email: str) -> Dict:
        self.register_attributes['family_name'] = family_name
        self.register_attributes['family_address'] = family_address
        self.register_attributes['phone'] = phone
        self.register_attributes['email'] = email
        
        return{
            "type" : "Family",
            "count": 1,
            "attributes": [
                {"family_name": family_name,
                "family_address": family_address,
                "phone": phone,
                "email": email}
            ]
        }