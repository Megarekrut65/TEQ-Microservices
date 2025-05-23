import re
from jinja2 import Environment, FileSystemLoader


ASSERT_MAP = {
    "float": "assertFloat",
    "integer": "assertEquals",
    "string": "assertEquals",
    "bool": "assertEquals",
    "sequence": "assertEquals",
}

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("testing_template.j2")

def make_testing_script(script, test_script):
    return f"""
{test_script}
    
{script}
"""

def get_function_name(signature):
    pattern = (
        r"(?:public\s+|private\s+|protected\s+)?"
        r"(?:static\s+)?"
        r"(?:final\s+)?"
        r"(?:java\.util\.)?"
        r"(?:int|long|float|double|boolean|char|byte|short|void|String|"
        r"List|Map|Set|Queue)(?:<[^>]+>)?\s+"
        r"(\w+)\s*\("
    )
    match = re.search(pattern, signature)
    return match.group(1) if match else "unknownFunction"

def make_test_case(function_structure, function_type, unittests):
    function_name = get_function_name(function_structure)

    rendered = template.render(
        tests=[
            {
                "prefix": test.prefix,
                "call": f"Solution.{function_name}({test.in_test})",
                "expected": test.out_test,
                "assert_func": ASSERT_MAP[function_type]
            }
            for test in unittests
        ]
    )
    return rendered

