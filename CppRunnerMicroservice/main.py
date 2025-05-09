import decouple
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.code_runner import run_code
from app.models import ScriptRequest

app = FastAPI()
origins = [
    decouple.config("ORIGIN")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/")
async def run(request: ScriptRequest):
    if request.script == "":
        return {"error":"File is empty"}

    res = await run_code(request.script)

    return res