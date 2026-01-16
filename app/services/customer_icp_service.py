from sqlalchemy.orm import Session
from datetime import datetime

from app.models.customer import SSCustomer
from app.models.customer_ICP import SSCustomerICP
from app.models.industry_ICP import SSICPIndustry
from app.models.geography_ICP import SSICPGeography
from app.models.buyingPersona_ICP import SSICPBuyingPersona
from app.models.companySize_ICP import SSICPCOMPANYSize

from app.repositories.customerRepository import CustomerRepository
from app.repositories.customerICPRepository import CustomerICPRepository
from app.repositories.icpAttributesRepository import ICPAttributesRepository

class CustomerICPService:

    @staticmethod
    def create_customer_with_icp(db: Session, request):
        try:
            # 1️ Create Customer
            customer = SSCustomer(
                company_name=request.company_name,
                company_url=str(request.company_url),
                created_by=request.created_by,
                created_date=datetime.utcnow()
            )
            customer = CustomerRepository.create(db, customer)

            # 2️ Create Customer ICP
            icp = SSCustomerICP(
                customer_id=customer.company_id,
                business_model=request.icp.business_model,
                competitive_positioning=request.icp.competitive_positioning,
                go_to_market_strategy=request.icp.go_to_market_strategy,
                key_recommendations=request.icp.key_recommendations,
                created_by=request.created_by,
                created_date=datetime.utcnow()
            )
            icp = CustomerICPRepository.create(db, icp)

            # 3️ Industry
            industry = SSICPIndustry(
                customer_icp_id=icp.customer_icp_id,
                name=request.icp.industry,
                created_by=request.created_by
            )
            ICPAttributesRepository.save_industry(db, industry)

             # 4️ Geography
            geography = SSICPGeography(
                customer_icp_id=icp.customer_icp_id,
                name=request.icp.geography,
                created_by=request.created_by
            )
            ICPAttributesRepository.save_geography(db, geography)

            # 5️ Buying Persona
            buyingpersona = SSICPBuyingPersona(
                customer_icp_id=icp.customer_icp_id,
                name=request.icp.buying_persona,
                created_by=request.created_by
            )
            ICPAttributesRepository.save_buying_persona(db, buyingpersona)

            # 6️ Company Size
            company_size = SSICPCOMPANYSize(
                customer_icp_id=icp.customer_icp_id,
                range=request.icp.company_size,
                created_by=request.created_by
            )
            ICPAttributesRepository.save_company_size(db, company_size)

            db.commit()

            return customer.company_id, icp.customer_icp_id

        except Exception as ex:
            db.rollback()
            raise ex