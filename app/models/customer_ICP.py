from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP, String
from datetime import datetime
from app.database.base import Base

class SSCustomerICP(Base):
    __tablename__ = "SS_CUSTOMER_ICP"

    customer_icp_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("SS_CUSTOMER.company_id"))
    business_model = Column(Text)
    competitive_positioning = Column(Text)
    go_to_market_strategy = Column(Text)
    key_recommendations = Column(Text)
    created_date = Column(TIMESTAMP, default=datetime.utcnow)
    created_by = Column(String(100))
    updated_date = Column(TIMESTAMP)
    updated_by = Column(String(100))