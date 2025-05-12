from fastapi import FastAPI, HTTPException

from app.models import ScriptRequest
from app.test_runner import run_tests
from app.utility import make_test_case

app = FastAPI()

@app.post("/")
def test(request: ScriptRequest):
    test_script = make_test_case(request.function_structure, request.function_type, request.unittests)

    try:
        passed, failures, total = run_tests(request.script, test_script)
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))

    return {
        "passed": passed,
        "failures": failures,
        "totalTests": total,
        "testScript": test_script,
    }
