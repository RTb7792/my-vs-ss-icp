from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from datetime import datetime
from app.database.base import Base

class SSICPCOMPANYSize(Base):
    __tablename__ = "SS_ICP_COMPANY_SIZE"

    icp_company_size_id = Column(Integer, primary_key=True)
    customer_icp_id = Column(Integer, ForeignKey("SS_CUSTOMER_ICP.customer_icp_id"))
    range = Column(String(50))
    created_date = Column(TIMESTAMP, default=datetime.utcnow)
    created_by = Column(String(100))
    updated_date = Column(TIMESTAMP)
    updated_by = Column(String(100))