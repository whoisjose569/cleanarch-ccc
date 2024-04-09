from typing import Dict

class MonthlyIncomeFinderSpy:
    def __init__(self) -> None:
        self.find_attributes = {}
    
    def find(self, family_id: int):
        self.find_attributes["family_id"] = family_id
        
        return {
            "type": "MonthlyIncome",
            "count": 1,
            "attributes": [
                {"family_id": family_id, "income": 200, "date": "2000-05-02"}
            ]
        }