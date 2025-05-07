import re

ASERT_MAP = {
    "float": "ASSERT_FLOAT_EQ_CUSTOM",
    "integer": "ASSERT_EQ",
    "string": "ASSERT_EQ",
    "bool": "ASSERT_EQ",
}

def make_assert_cpp(f_call, f_type, f_res):
    assert_macro = ASERT_MAP[f_type]
    return f"{assert_macro}({f_call}, {f_res});"

def get_fun_name(f_struct):
    match = re.search(r"\b(?:float|int|bool|string|double|auto|void)\s+(\w+)\s*\(", f_struct)
    return match.group(1) if match else "unknown_func"

def make_test_fun_cpp(index, f_name, f_type, unittest):
    f_call = f"{f_name}({unittest.in_test})"
    return f"""
TEST(TestCase, TestFun_{unittest.prefix}{index}) {{
    {make_assert_cpp(f_call, f_type, unittest.out_test)}
}}
"""

def make_testing_script(script, test_script):
    return f"""
{script}

// Test cases
{test_script}

int main(int argc, char **argv) {{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}}
"""

def make_test_case(f_struct, f_type, unittests):
    f_name = get_fun_name(f_struct)
    tests = [make_test_fun_cpp(i + 1, f_name, f_type, unittest) for i, unittest in enumerate(unittests)]

    return f"""
#include <string>
#include <cmath>
#include <gtest/gtest.h>
#define ASSERT_FLOAT_EQ_CUSTOM(a, b) ASSERT_NEAR(a, b, 1e-6)

{''.join(tests)}
"""

