# Given two positive integers. Write a python function to return the greatest common divisor of the given numbers.


def find_gcd(num1, num2):
    if num1 == 0 or num2 == 0:
        return num1 + num2
    elif num1 == num2:
        return num1
    elif num1 > num2:
        return find_gcd(num1 - num2, num2)
    else:
        return find_gcd(num1, num2 - num1)


num1 = 2800
num2 = 800
print(find_gcd(num1, num2))
