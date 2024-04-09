from src.infra.db.repositories.family_repository import FamilyRepository
from src.data.use_cases.family_register import FamilyRegister
from src.presentation.controllers.family_register_controller import FamilyRegisterController

def family_register_composer():
    repository = FamilyRepository()
    use_case = FamilyRegister(repository)
    controller = FamilyRegisterController(use_case)
    
    return controller.handle