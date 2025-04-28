import json

import decouple
import requests

PYTHON_URL = decouple.config("PYTHON_URL")

def make_testing_script(script, test_script):
    code = f"""

{script}

{test_script}

def unittest_wrapper():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCase)
    
    import io
    import json
    
    fake_output = io.StringIO()
    runner = unittest.TextTestRunner(stream=fake_output,verbosity=0)
    result = runner.run(suite)
    return json.dumps({{
        "passed": result.wasSuccessful(),
        "failures": [(case.id(), err) for case, err in result.failures],
        "errors": [(case.id(), err) for case, err in result.errors],
        "total_tests": result.testsRun
    }})
    
print(unittest_wrapper())
    """

    return code

def run_tests(script, test_script):

    code = make_testing_script(script, test_script)
    response = requests.post(PYTHON_URL, json={"script": code})

    if response.status_code != 200:
        return response.text, 400

    obj = response.json()
    if obj.get("error", "") != "":
        return obj["error"], 400

    output = json.loads(obj["output"])
    if "failures" not in output or "errors" not in output \
            or "passed" not in output or "total_tests" not in output:
        return "Testing error", 400

    failures_info = []
    for case, err in output["failures"] + output["errors"]:
        test_name = case.split(".")[-1]
        reason_lines = err.strip().split("\n")
        if reason_lines:
            last_line = reason_lines[-1]
        else:
            last_line = "Unknown Error"
        failures_info.append({
            "test_name": test_name,
            "reason": last_line
        })

    return {
        "passed": output["passed"],
        "failures":failures_info,
        "total_tests": output["total_tests"]
    }, 200