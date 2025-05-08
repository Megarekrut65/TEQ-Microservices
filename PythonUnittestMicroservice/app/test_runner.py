import json
import re

import decouple
import requests

from .utility import make_testing_script

RUNNER_URL = decouple.config("RUNNER_URL")


def extract_reason(err):
    """
    Extract reason for failure
    :param err:
    :return:
    """
    match = re.search(r"AssertionError:.*", err, re.DOTALL)
    if match:
        return match.group()

    return err

def extract_failures(output):
    """
    Extract all failures from output
    :param output:
    :return:
    """
    failures_info = []
    for case, err in output["failures"] + output["errors"]:
        test_name = case.split(".")[-1]
        reason = extract_reason(err)

        failures_info.append({
            "testName": test_name,
            "reason": reason
        })
    return failures_info

def run_tests(script, test_script):
    code = make_testing_script(script, test_script)

    response = requests.post(RUNNER_URL, json={"script": code})

    if response.status_code != 200:
        raise Exception(response.text)

    obj = response.json()
    if obj.get("error", "") != "":
        raise Exception(obj["error"])

    output = json.loads(obj["output"])
    if "failures" not in output or "errors" not in output \
            or "passed" not in output or "total_tests" not in output:
        raise Exception("Testing error")

    failures = extract_failures(output)

    return output["passed"], failures, output["total_tests"]