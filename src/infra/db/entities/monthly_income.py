from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.db.settings.base import Base

class MonthlyIncome(Base):
    __tablename__ = "monthly_income"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    income = Column(Float, nullable=False)
    date = Column(String, nullable=False)
    
    family_id = Column(Integer, ForeignKey('family.id', name='fk_monthly_income_family'))
    family = relationship('Family', back_populates='monthly_income')