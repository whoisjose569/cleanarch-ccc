from typing import List
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.family import Family as FamilyEntity
from src.data.interfaces.family_repository import FamilyRepositoryInterface
from src.domain.models.family import Family
from src.domain.providers import hash_provider, token_provider

class FamilyRepository(FamilyRepositoryInterface):
    
    @classmethod
    def insert_family(cls, family_name: str, senha: str, phone: str, email: str) -> None:
        password = hash_provider.generate_hash(senha)
        with DBConnectionHandler() as database:
            try:
                new_registry = FamilyEntity(
                    family_name = family_name,
                    senha = password,
                    phone = phone,
                    email = email
                )
                existing_family = database.session.query(FamilyEntity).filter(FamilyEntity.email == email).first()
                if existing_family:
                    raise Exception 
                database.session.add(new_registry),
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    @classmethod
    def select_family(cls, email: str) -> List[Family]:
        with DBConnectionHandler() as database:
            try:
                family = (
                    database.session.query(FamilyEntity).filter(FamilyEntity.email == email).all()
                )
                return family
            except Exception as exception:
                database.session.rollback()
                raise exception
