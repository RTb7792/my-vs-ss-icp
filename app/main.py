from fastapi import FastAPI
from app.api.v1.customer_icp_api import router as customer_icp_router
from app.database.session import engine
from app.database.base import Base

from app.models.customer import SSCustomer
from app.models.customer_ICP import SSCustomerICP
from app.models.industry_ICP import SSICPIndustry
from app.models.geography_ICP import SSICPGeography
from app.models.buyingPersona_ICP import SSICPBuyingPersona
from app.models.companySize_ICP import SSICPCOMPANYSize

# Base.metadata.create_all(bind=engine)

app = FastAPI(title="SS ICP STRATEGY")

app.include_router(customer_icp_router)

@app.get("/health")
def health_check():
    return {"status": "UP"}








