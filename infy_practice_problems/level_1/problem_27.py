# Given 2 positive integers, write a python function to return True if one of them is 10 or if their sum is 10, else return False.

def check_for_ten(num1, num2):
    res = False
    if num1 == 10 or num2 == 10:
        res = True
    elif num1 + num2 == 10:
        res = True
    return res


print(check_for_ten(10, 9))
