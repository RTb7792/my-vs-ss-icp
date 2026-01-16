from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.customerValidation import CustomerCreate
from app.schemas.response import CreateResponse
from app.services.customer_icp_service import CustomerICPService

router = APIRouter(
    prefix="/api/v1/customer",
    tags=["Customer ICP"]
)

@router.post(
    "/icp",
    response_model=CreateResponse,
    status_code=status.HTTP_201_CREATED
)
def create_customer_icp(
    request: CustomerCreate,
    db: Session = Depends(get_db)
):
    try:
        company_id, customer_icp_id = CustomerICPService.create_customer_with_icp(
            db, request
        )

        return CreateResponse(
            status="SUCCESS",
            company_id=company_id,
            customer_icp_id=customer_icp_id,
            message="Customer and ICP details saved successfully"
        )

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )