import json
import re

import decouple
import requests

from .utility import make_testing_script

RUNNER_URL = decouple.config("RUNNER_URL")

def extract_reason(err):
    match = re.search(r"AssertionError:.*", err, re.DOTALL)
    if match:
        return match.group()

    return err

def run_tests(script, test_script):
    code = make_testing_script(script, test_script)

    response = requests.post(RUNNER_URL, json={"script": code})

    if response.status_code != 200:
        raise Exception(response.text)

    obj = response.json()
    if obj.get("error", "") != "":
        raise Exception(obj["error"])

    output = json.loads(obj["output"])

    if "failures" not in output or "passed" not in output or "totalTests" not in output:
        raise Exception("Testing error")

    return output["passed"], output["failures"], output["totalTests"]