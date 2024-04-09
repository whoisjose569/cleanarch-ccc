from src.infra.db.repositories.family_repository import FamilyRepository
from src.data.use_cases.family_finder import FamilyFinder
from src.presentation.controllers.family_finder_controller import FamilyFinderController

def family_finder_composer():
    repository = FamilyRepository()
    use_case = FamilyFinder(repository)
    controller = FamilyFinderController(use_case)
    
    return controller.handle