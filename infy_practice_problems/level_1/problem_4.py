# Given a list of numbers,
# write a python function which returns true if one of the first 4 elements in the list is 9. Otherwise it should return false.
#
# The length of the list can be less than 4 also.

def find_nine(nums):
    res = False
    if len(nums) <= 4:
        for i in nums:
            if i == 9:
                res = True
    else:
        for i in nums[0:4]:
            if i == 9:
                res = True
    return res


nums = [1, 9, 4, 5, 6]
print(find_nine(nums))
