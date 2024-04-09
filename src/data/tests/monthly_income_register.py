from typing import Dict

class MonthlyIncomeRegisterSpy:
    def __init__(self) -> None:
        self.register_attributes = {}
    
    def register(self, family_id: int, income: float, date: str) -> Dict:
        self.register_attributes["family_id"] = family_id
        self.register_attributes["income"] = income
        self.register_attributes["date"] = date
    
        return {
            "type": "MonthlyIncome",
            "count": 1,
            "attributes": [
                {"family_id": family_id,
                "income": income,
                "date": date}
            ]
        }