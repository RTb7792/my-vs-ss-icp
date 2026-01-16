from pydantic import BaseModel, HttpUrl
from typing import Optional

class ICPCreate(BaseModel):
    business_model: Optional[str]
    competitive_positioning: Optional[str]
    go_to_market_strategy: Optional[str]
    key_recommendations: Optional[str]

    industry: str
    geography: str
    buying_persona: str
    company_size: str


class CustomerCreate(BaseModel):
    company_name: str
    company_url: HttpUrl
    created_by: str
    icp: ICPCreate