# Given a list of numbers, write a python function to exchange the first n/2 elements of a list with the last n/2 elements.
# The function should return the new list.
# n represents the number of elements in the list. Assume that it will always be even.
# Sample Input                            Expected Output
# ------------                           -------------------
# [1,2,3,4,5,6,7,8,9,10]              [10,9,8,7,6,1,2,3,4,5]


def exchange_list(number_list):
    mid_idx = len(number_list) // 2
    first_list = number_list[mid_idx:]
    first_list.reverse()
    second_list = number_list[0:mid_idx]
    first_list.extend(second_list)

    return first_list


number_list = [1, 2, 3, 4, 5, 6]
print(exchange_list(number_list))
