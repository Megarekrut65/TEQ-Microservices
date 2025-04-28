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

@app.post("/java/run")
async def run(request: ScriptRequest):
    res = await run_code(request.script)

    return res