from app.core.exceptions import BusinessException
from sqlalchemy.orm import Session
from app.models.customer import SSCustomer
from app.models.customer_ICP import SSCustomerICP
from app.models.industry_ICP import SSICPIndustry
from app.models.geography_ICP import SSICPGeography
from app.models.buyingPersona_ICP import SSICPBuyingPersona
from app.models.companySize_ICP import SSICPCOMPANYSize
from app.schemas.icp_request import ICPSubmitRequest

def submit_icp(db, request):
    try:
        # All inserts here
        db.commit()
    except Exception as e:
        db.rollback()
        raise BusinessException("ICP submission failed")

def submit_icp(db: Session, request: ICPSubmitRequest):
    try:
        customer = SSCustomer(
            company_name=request.company.name,
            company_url=request.company.url,
            created_by=request.created_by
        )
        db.add(customer)
        db.flush()  # get company_id 

        icp = SSCustomerICP(
            customer_id=customer.company_id,
            business_model=request.icp.business_model,
            competitive_positioning=request.icp.competitive_positioning,
            go_to_market_strategy=request.icp.go_to_market_strategy,
            key_recommendations=request.icp.key_recommendations,
            created_by=request.created_by
        )
        db.add(icp)
        db.flush()  # get customer_icp_id

        for item in request.industries:
            db.add(SSICPIndustry(
                customer_icp_id=icp.customer_icp_id,
                name=item,
                created_by=request.created_by
            ))

        for item in request.geographies:
            db.add(SSICPGeography(
                customer_icp_id=icp.customer_icp_id,
                name=item,
                created_by=request.created_by
            ))

        for item in request.buying_personas:
            db.add(SSICPBuyingPersona(
                customer_icp_id=icp.customer_icp_id,
                name=item,
                created_by=request.created_by
            ))

        for item in request.company_size:
            db.add(SSICPCOMPANYSize(
                customer_icp_id=icp.customer_icp_id,
                range=item,
                created_by=request.created_by
            ))

        db.commit()
        return {"message": "ICP submitted successfully"}

    except Exception as e:
        db.rollback()
        raise e    