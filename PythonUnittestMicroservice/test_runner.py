import json
import re

import decouple
import requests

from utility import make_testing_script

PYTHON_URL = decouple.config("PYTHON_URL")

def extract_reason(err):
    match = re.search(r"AssertionError:.*", err, re.DOTALL)
    if match:
        return match.group()

    return err

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
        reason = extract_reason(err)

        failures_info.append({
            "testName": test_name,
            "reason": reason
        })

    return {
        "passed": output["passed"],
        "failures":failures_info,
        "totalTests": output["total_tests"]
    }, 200