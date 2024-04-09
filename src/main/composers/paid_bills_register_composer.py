from src.infra.db.repositories.paid_bills_repository import PaidBillsRepository
from src.data.use_cases.paid_bills_register import PaidBillsRegister
from src.presentation.controllers.paid_bills_register_controller import PaidBillsRegisterController

def paid_bills_register_composer():
    repository = PaidBillsRepository()
    use_case = PaidBillsRegister(repository)
    controller = PaidBillsRegisterController(use_case)
    
    return controller.handle