from pydantic import BaseModel, Field

class UnitTestRequest(BaseModel):
    script: str = Field(..., alias="script", description="User's function code as a string")
    test_script: str = Field(..., alias="test_script", description="User's testing code as a string")

    class Config:
        validate_by_name = True
