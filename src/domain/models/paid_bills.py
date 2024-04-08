class PaidBills:
    def __init__(self, id: int,family_id: int, type: str, value: float, payment_date: str) -> None:
        self.id = id
        self.family_id = family_id
        self.type = type
        self.value = value
        self.payment_date = payment_date
