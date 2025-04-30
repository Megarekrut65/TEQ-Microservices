import re

def make_testing_script(script, test_script):
    return f"""

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

ASERT_MAP = {
    "float": "assertAlmostEqual",
    "integer": "assertEqual",
    "string": "assertEqual",
    "bool": "assertEqual",
}

def make_assert(f_call, f_type, f_res):
    assert_call = ASERT_MAP[f_type]

    return f"self.{assert_call}({f_call}, {f_res})"

def get_fun_name(f_struct):
    match = re.search(r'def\s+(\w+)\s*\(', f_struct)
    if match:
        return match.group(1)

    return f_struct

def make_test_fun(index, f_name, f_type, unittest):
    f_call = f"{f_name}({unittest.in_test})"

    return f"""
    def test_fun_{index}(self):
        {make_assert(f_call, f_type, unittest.out_test)}       
"""

def make_test_case(f_struct, f_type, unittests):
    f_name = get_fun_name(f_struct)

    tests = [make_test_fun(i+1, f_name, f_type, unittest) for i, unittest in enumerate(unittests)]
    return f"""
import unittest
class TestCase(unittest.TestCase):
{''.join(tests)}
    """
