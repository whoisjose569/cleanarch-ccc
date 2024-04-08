from sqlalchemy import Column, String, Integer
from src.infra.db.settings.base import Base
from sqlalchemy.orm import relationship
from .monthly_income import MonthlyIncome
from .paid_bills import PaidBills

class Family(Base):
    __tablename__ = "family"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    family_name = Column(String, nullable=False)
    family_address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    
    monthly_income = relationship('MonthlyIncome', back_populates='family')
    paid_bills = relationship('PaidBills', back_populates='family')