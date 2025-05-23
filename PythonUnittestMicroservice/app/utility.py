import re
from jinja2 import Environment, FileSystemLoader

def make_testing_script(script, test_script):
    return f"""
{script}

{test_script}
"""

ASSERT_MAP = {
    "float": "assertAlmostEqual",
    "integer": "assertEqual",
    "string": "assertEqual",
    "bool": "assertEqual",
    "sequence": "assertEqual",
}

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("testing_template.j2")

def get_function_name(function_code):
    match = re.search(r"def\s+(\w+)\s*\(", function_code)
    return match.group(1) if match else function_code

def make_test_case(f_struct, f_type, unittests):
    function_name = get_function_name(f_struct)

    rendered = template.render(
        tests=[
            {
                "prefix": test.prefix,
                "call": f"{function_name}({test.in_test})",
                "expected": test.out_test,
                "assert_func": ASSERT_MAP[f_type]
            }
            for test in unittests
        ]
    )
    return rendered