from sqlalchemy import Column, Integer, String, TIMESTAMP
from datetime import datetime
from app.database.base import Base

class SSCustomer(Base):
    __tablename__ = "SS_CUSTOMER"

    company_id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(150), nullable=False)
    company_url = Column(String(255), nullable=False)
    created_date = Column(TIMESTAMP, default=datetime.utcnow)
    created_by = Column(String(100))
    updated_date = Column(TIMESTAMP)
    updated_by = Column(String(100))