from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.db.settings.base import Base

class PaidBills(Base):
    __tablename__ = "paid_bills"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    payment_date = Column(String, nullable=False)
    
    family_id = Column(Integer, ForeignKey('family.id', name='fk_paid_bills_family'))
    family = relationship('Family', back_populates='paid_bills')