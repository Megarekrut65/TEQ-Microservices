import decouple
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models import UnitTestRequest
from test_runner import run_tests

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

@app.post("/python/test")
def run(request: UnitTestRequest):
    if request.script == "":
        return {"error":"Script file is empty"}

    response, status = run_tests(request.script, request.test_script)

    if status != 200:
        return HTTPException(status_code=status, detail=response)

    return response
