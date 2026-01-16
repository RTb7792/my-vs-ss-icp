from sqlalchemy.orm import Session
from app.models.industry_ICP import SSICPIndustry
from app.models.geography_ICP import SSICPGeography
from app.models.buyingPersona_ICP import SSICPBuyingPersona
from app.models.companySize_ICP import SSICPCOMPANYSize

class ICPAttributesRepository:

    @staticmethod
    def save_industry(db: Session, industry: SSICPIndustry):
        db.add(industry)

    @staticmethod
    def save_geography(db: Session, geography: SSICPGeography):
        db.add(geography)

    @staticmethod
    def save_buying_persona(db: Session, buyingPersona: SSICPBuyingPersona):
        db.add(buyingPersona)

    @staticmethod
    def save_company_size(db: Session, company_size: SSICPCOMPANYSize):
        db.add(company_size)
