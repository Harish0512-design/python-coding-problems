# Given two numbers, write a python function which returns true if first number is a seed of second number. Otherwise it returns false.
# A number X is said to be a seed of number Y, if multiplying X by its each digit equates to Y
# For example, 123 is a seed of 738 as 123*1*2*3 = 738.


def seed_no(number, ref_no):
    res = False
    temp = number
    for i in str(temp):
        temp *= int(i)
    if temp == ref_no:
        res = True
    return res


number = 123
ref_no = 738
print(seed_no(number, ref_no))
