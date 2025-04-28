from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from code_runner import run_code
from models import ScriptRequest

app = FastAPI()
origins = [
    "http://localhost:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/python/run")
async def run(request: ScriptRequest):
    if request.script == "":
        return {"error":"File is empty"}

    res = await run_code(request.script)

    return res