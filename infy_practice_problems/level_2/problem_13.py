# Write a python function which accepts three numbers and returns True if
# a. one of the three numbers is "close" to any one of the other numbers (differing from a number by at most 1), and
# b.Number that is left out is "far", differing from both other values by 2 or more.
# Return false if the above mentioned conditions are not satisfied.
# SampleInput                 Expected Output
# 4,1,3                             True
# 5,6,7                             False

def close_number(num1, num2, num3):
    res = False
    if num1-num2 == 0 or abs(num1-num2) == 1:
        if abs(num1-num3) > 1 and abs(num2-num3) > 1:
            res = True

    elif num2-num3 == 0 or abs(num2-num3) == 1:
        if abs(num2-num1) > 1 and abs(num2-num1) > 1:
            res = True

    elif num3-num1 == 0 or abs(num3-num1) == 1:
        if abs(num1-num2) > 1 and abs(num3-num2) > 1:
            res = True

    return res


print(close_number(5, 4, 2))