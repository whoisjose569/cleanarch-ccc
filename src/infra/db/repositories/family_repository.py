from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.family import Family as FamilyEntity

class FamilyRepository:
    
    @classmethod
    def insert_family(cls, family_name: str, family_adress: str, phone: str, email: str) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = FamilyEntity(
                    family_name = family_name,
                    family_address = family_adress,
                    phone = phone,
                    email = email
                )
                database.session.add(new_registry),
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
