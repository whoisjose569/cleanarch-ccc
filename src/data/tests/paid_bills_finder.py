from typing import Dict

class PaidBillsFinderSpy:
    def __init__(self) -> None:
        self.find_attributes = {}
    
    def find_by_family_id(self, family_id: int) -> Dict:
        self.find_attributes["family_id"] = family_id
        return {
            "type": "PaidBills",
            "count": 1,
            "attributes": [
                {"family_id": family_id, "type": "Luz", "value": 200, "payment_date": "2000-05-02"}
            ]
        }
    
    def find_by_value(self, value: float) -> Dict:
        self.find_attributes["value"] = value
        return {
            "type": "PaidBills",
            "count": 1,
            "attributes": [
                {"family_id": 1, "type": "Luz", "value": value, "payment_date": "2000-05-02"}
            ]
        }
    
    def find_by_type(self, type: str) -> Dict:
        self.find_attributes["type"] = type
        return {
            "type": "PaidBills",
            "count": 1,
            "attributes": [
                {"family_id": 1, "type": type, "value": 200, "payment_date": "2000-05-02"}
            ]
        }
    
    def find_by_payment_date(self, payment_date: str) -> Dict:
        self.find_attributes["payment_date"] = payment_date
        return {
            "type": "PaidBills",
            "count": 1,
            "attributes": [
                {"family_id": 1, "type": "Luz", "value": 200, "payment_date": payment_date}
            ]
        }