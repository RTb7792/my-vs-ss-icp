from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.schemas.icp_request import ICPSubmitRequest
from app.services.icp_service import submit_icp

router = APIRouter(prefix="/api/v1/icp", tags=["ICP"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/submit")
def submit(request: ICPSubmitRequest, db: Session = Depends(get_db)):
    return submit_icp(db, request)