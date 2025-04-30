import decouple
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models import ScriptRequest
from test_runner import run_tests
from utility import make_testing_script, make_test_case

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
def run(request: ScriptRequest):
    test_script = make_test_case(request.function_structure, request.function_type, request.unittests)
    response, status = run_tests(request.script, test_script)

    if status != 200:
        return HTTPException(status_code=status, detail=response)

    response["testCase"] = test_script
    return response
