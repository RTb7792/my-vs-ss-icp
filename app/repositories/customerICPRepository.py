from sqlalchemy.orm import Session
from app.models.customer_ICP import SSCustomerICP

class CustomerICPRepository:

    @staticmethod
    def create(db: Session, icp: SSCustomerICP):
        db.add(icp)
        db.flush()
        return icp