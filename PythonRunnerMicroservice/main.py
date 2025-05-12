from fastapi import FastAPI

from app.code_runner import run_code
from app.models import ScriptRequest

app = FastAPI()

@app.post("/")
async def run(request: ScriptRequest):
    if request.script == "":
        return {"error":"File is empty"}

    res = await run_code(request.script)

    return res