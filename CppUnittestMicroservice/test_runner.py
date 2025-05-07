import json
import re

import decouple
import requests

from utility import make_testing_script

CPP_URL = decouple.config("CPP_URL")

def extract_reason(err):
    match = re.search(r"AssertionError:.*", err, re.DOTALL)
    if match:
        return match.group()

    return err

def run_tests(script, test_script):
    code = make_testing_script(script, test_script)
    response = requests.post(CPP_URL, json={"script": code})

    if response.status_code != 200:
        return response.text, 400

    obj = response.json()
    if obj.get("error", "") != "":
        return obj["error"], 400

    gtest_output=obj["output"]
    total_tests_match = re.search(r"\[==========\] (\d+) tests? from", gtest_output)
    total_tests = int(total_tests_match.group(1)) if total_tests_match else 0

    passed_tests = re.findall(r"\[\s+OK\s+\] ([\w\.]+)", gtest_output)
    total_passed = len(passed_tests)
    failed_tests = re.findall(r"\[\s+FAILED\s+\] ([\w\.]+)", gtest_output)

    error_blocks = re.findall(
        r"\[ RUN\s+\] ([\w\.]+)\n(.*?)(?=\[\s+(?:OK|FAILED)\s+\])", gtest_output, re.DOTALL
    )

    failures_info = []
    for test_name, message in error_blocks:
        if test_name in failed_tests:
            failures_info.append({
                "testName": test_name,
                "reason": message.strip()
            })

    return {
        "passed": total_tests == total_passed,
        "failures":failures_info,
        "totalTests": total_tests
    }, 200