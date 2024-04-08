class Family:
    def __init__(self, id: int, family_name: str, family_address: str, phone: str, email: str):
        self.id = id
        self.family_name = family_name
        self.family_address = family_address
        self.phone = phone
        self.email = email
        self.monthly_income = []
        self.paid_bills = []
