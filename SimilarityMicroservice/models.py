from pydantic import BaseModel, Field

class SimilarityRequest(BaseModel):
    text1: str = Field(..., alias="text1")
    text2: str = Field(..., alias="text2")

    class Config:
        validate_by_name = True

