# Write a python function which accepts a list of numbers and returns true, if 1, 2, 3 appears in sequence in the list.
#
# Otherwise, it should return false.

import re


def list123(nums):
    res = False
    nums_string = ''.join([str(x) for x in nums])
    if '123' in nums_string:
        res = True
    return res


nums = [1, 2, 3, 4, 5]
print(list123(nums))
