from pydantic import BaseModel, Field

class ScriptRequest(BaseModel):
    script: str = Field(..., alias="script")

    class Config:
        populate_by_name  = True

