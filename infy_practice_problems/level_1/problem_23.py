# Write a python function to find out whether a number is divisible by the sum of its digits.
# If so return True,else return False.

def divisible_by_sum(number):
    res = False
    sum_of_digits = 0
    for num in str(number):
        sum_of_digits += int(num)
    if number % sum_of_digits == 0:
        res = True
    return res


number = 42
print(divisible_by_sum(number))
