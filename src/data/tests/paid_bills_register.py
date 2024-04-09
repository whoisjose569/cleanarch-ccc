from typing import Dict

class PaidBillsRegisterSpy:
    def __init__(self) -> None:
        self.register_attributes = {}
    
    def register(self, family_id: int, type: str, value: float, payment_date: str) -> Dict:
        self.register_attributes["family_id"] = family_id
        self.register_attributes["type"] = type
        self.register_attributes["value"] = value
        self.register_attributes["payment_date"] = payment_date
        
        return{
            "type": "PaidBills",
            "count": 1,
            "attributes": [
                {"family_id": family_id,
                "type": type,
                "value": value,
                "payment_date": payment_date}
            ]
        }