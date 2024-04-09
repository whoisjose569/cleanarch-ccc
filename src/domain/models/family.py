class Family:
    def __init__(self, id: int, family_name: str, senha: str, phone: str, email: str):
        self.id = id
        self.family_name = family_name
        self.senha = senha
        self.phone = phone
        self.email = email
        self.monthly_income = []
        self.paid_bills = []
