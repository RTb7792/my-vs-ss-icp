from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from datetime import datetime
from app.database.base import Base

class SSICPBuyingPersona(Base):
    __tablename__ = "SS_ICP_BUYING_PERSONA"

    icp_buying_persona_id = Column(Integer, primary_key=True)
    customer_icp_id = Column(Integer, ForeignKey("SS_CUSTOMER_ICP.customer_icp_id"))
    name = Column(String(100))
    created_date = Column(TIMESTAMP, default=datetime.utcnow)
    created_by = Column(String(100))
    updated_date = Column(TIMESTAMP)
    updated_by = Column(String(100))