from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.monthly_income import MonthlyIncome as MonthlyIncomeEntity

class MonthlyIncomeRepository:
    
    @classmethod
    def insert_monthly_income(cls, family_id: int, income: float, date: str):
        with DBConnectionHandler() as database:
            try:
                new_registry = MonthlyIncomeEntity(
                    family_id = family_id,
                    income = income,
                    date = date
                )
                database.session.add(new_registry),
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    @classmethod
    def select_monthly_income(cls, family_id: int):
        with DBConnectionHandler() as database:
            try:
                monthly_income = (
                    database.session.query(MonthlyIncomeRepository).filter(MonthlyIncomeEntity.family_id == family_id).all()
                )
                return monthly_income
            except Exception as exception:
                database.session.rollback()
                raise exception