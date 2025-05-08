from pydantic import BaseModel, Field

class SimilarityRequest(BaseModel):
    code1: str = Field(..., alias="code1")
    code2: str = Field(..., alias="code2")

    class Config:
        validate_by_name = True

