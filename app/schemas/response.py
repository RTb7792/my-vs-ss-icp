from pydantic import BaseModel

class CreateResponse(BaseModel):
    status: str
    company_id: int
    customer_icp_id: int
    message: str
