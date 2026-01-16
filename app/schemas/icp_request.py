from pydantic import BaseModel
from typing import List

class Company(BaseModel):
    name: str
    url: str

class ICP(BaseModel):
    business_model: str
    competitive_positioning: str
    go_to_market_strategy: str
    key_recommendations: str

class ICPSubmitRequest(BaseModel):
    company: Company
    icp: ICP
    industries: List[str]
    geographies: List[str]
    buying_personas: List[str]
    company_size: List[str]
    created_by: str