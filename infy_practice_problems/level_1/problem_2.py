# Write a python function which accepts a string containing a pattern of brackets and returns true if the pattern of brackets is correct. Otherwise it returns false.
#
# The string of brackets is correct if it satisfies the following conditions:
# 1. Number of opening and closing brackets are equal.
# 2. Pattern should not start with closing bracket and end with opening bracket.
# )()((()()) -- False
# ()((())()) -- True

# lex_auth_0127135773590405121141

def bracket_pattern(input_str):
    # Remove pass and write your code here
    opening_braces = input_str.count('(')
    closing_braces = input_str.count(')')
    res = False
    if opening_braces == closing_braces:
        if not (input_str.startswith(')') or input_str.endswith('(')):
            res = True
    return res

input_str = ")(())("
print(bracket_pattern(input_str))
