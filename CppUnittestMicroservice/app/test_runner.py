import re

import decouple
import requests

from .utility import make_testing_script

RUNNER_URL = decouple.config("RUNNER_URL")


def extract_failures(error_blocks, failed_tests):
    failures_info = []
    for test_name, message in error_blocks:
        if test_name in failed_tests:
            failures_info.append({
                "testName": test_name,
                "reason": message.strip()
            })

    return failures_info

def extract_result(output):
    total_tests_match = re.search(r"\[==========\] (\d+) tests? from", output)
    total_tests = int(total_tests_match.group(1)) if total_tests_match else 0

    passed_tests = re.findall(r"\[\s+OK\s+\] ([\w\.]+)", output)
    total_passed = len(passed_tests)
    failed_tests = re.findall(r"\[\s+FAILED\s+\] ([\w\.]+)", output)

    error_blocks = re.findall(
        r"\[ RUN\s+\] ([\w\.]+)\n(.*?)(?=\[\s+(?:OK|FAILED)\s+\])", output, re.DOTALL
    )

    failures = extract_failures(error_blocks, failed_tests)

    return total_tests, total_passed, failures


def run_tests(script, test_script):
    code = make_testing_script(script, test_script)

    response = requests.post(RUNNER_URL, json={"script": code})

    if response.status_code != 200:
        raise Exception(response.text)

    obj = response.json()
    if obj.get("error", "") != "":
        raise Exception(obj["error"])

    gtest_output=obj["output"]
    total_tests, total_passed, failures = extract_result(gtest_output)

    return total_tests == total_passed, failures, total_tests