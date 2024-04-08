from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.paid_bills import PaidBills as PaidBillsEntity

class PaidBillsRepository:
    
    @classmethod
    def insert_paid_bills(cls, family_id: int, type: str, value: float, payment_date: str) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = PaidBillsEntity(
                    family_id = family_id,
                    type = type,
                    value = value,
                    payment_date = payment_date
                )
                database.session.add(new_registry),
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    @classmethod
    def select_paid_bill_by_type(cls, type: str):
        with DBConnectionHandler() as database:
            try:
                paid_bills = (
                    database.session.query(PaidBillsEntity).filter(PaidBillsEntity.type == type).all()
                )
                return paid_bills
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_paid_bill_by_value(cls, value: float):
        with DBConnectionHandler() as database:
            try:
                paid_bills = (
                    database.session.query(PaidBillsEntity).filter(PaidBillsEntity.value == value).all()
                )
                return paid_bills
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_paid_bill_by_payment_date(cls, payment_date: str):
        with DBConnectionHandler() as database:
            try:
                paid_bills = (
                    database.session.query(PaidBillsEntity).filter(PaidBillsEntity.payment_date == payment_date).all()
                )
                return paid_bills
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_paid_bill_by_family_id(cls, family_id: int):
        with DBConnectionHandler() as database:
            try:
                paid_bills = (
                    database.session.query(PaidBillsEntity).filter(PaidBillsEntity.family_id == family_id).first()
                )
                return paid_bills
            except Exception as exception:
                database.session.rollback()
                raise exception