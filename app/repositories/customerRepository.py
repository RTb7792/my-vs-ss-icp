from sqlalchemy.orm import Session
from app.models.customer import SSCustomer
class CustomerRepository:

    @staticmethod
    def create(db: Session, customer: SSCustomer):
        db.add(customer)
        db.flush()  # get generated ID
        return customer