import re
from jinja2 import Environment, FileSystemLoader

ASSERT_MAP = {
    "float": "ASSERT_FLOAT_EQ_CUSTOM",
    "integer": "ASSERT_EQ",
    "string": "ASSERT_EQ",
    "bool": "ASSERT_EQ",
}

def get_fun_name(f_struct):
    match = re.search(r"\b(?:float|int|bool|string|double|auto|void)\s+(\w+)\s*\(", f_struct)
    return match.group(1) if match else "unknown_func"

def make_test_case(f_struct, f_type, unittests):
    f_name = get_fun_name(f_struct)

    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("testing_template.j2")

    rendered = template.render(
        tests=[
            {
                "prefix": unittest.prefix,
                "call": f"{f_name}({unittest.in_test})",
                "expected": unittest.out_test,
                "assert_macro": ASSERT_MAP[f_type],
            }
            for unittest in unittests
        ]
    )
    return rendered

def make_testing_script(script, test_script):
    return f"""
{script}

{test_script}
"""
