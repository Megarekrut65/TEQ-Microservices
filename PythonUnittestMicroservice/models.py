from typing import List
from pydantic import BaseModel, Field

class UnitTest(BaseModel):
    in_test: str = Field(..., alias="inTest", max_length=500)
    out_test: str = Field(..., alias="outTest", max_length=200)

    class Config:
        populate_by_name = True  # allows using both in_test and inTest

class ScriptRequest(BaseModel):
    function_structure: str = Field("", alias="functionStructure", max_length=500)
    function_type: str = Field(..., alias="functionType", max_length=50)
    unittests: List[UnitTest] = Field(..., alias="publicUnittests")
    script: str = Field(..., max_length=5000)

    class Config:
        populate_by_name = True
