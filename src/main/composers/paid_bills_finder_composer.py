from src.infra.db.repositories.paid_bills_repository import PaidBillsRepository
from src.data.use_cases.paid_bills_finder import PaidBillsFinder
from src.presentation.controllers.paid_bills_finder_controller import PaidBillsFinderController

def paid_bills_finder_composer():
    repository = PaidBillsRepository()
    use_case = PaidBillsFinder(repository)
    controller = PaidBillsFinderController(use_case)
    
    return controller.handle