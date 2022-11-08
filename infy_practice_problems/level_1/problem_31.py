# Given a list of integers and a number. Write a python function to find and return the sum of the elements of the list.
# Note: Don't add the given number and also the numbers present before and after the given number in the list.
# Sample Input                         Sample Output
# -------------                       --------------
# l=[1,3,4,8], number = 3                 8
# l = [1,2,3,4,5,6] number = 2            15


def sum_of_elements(num_list, number):
    result_sum = 0
    for i in range(len(num_list)):
        if i == 0:
            if num_list[i] != number and num_list[i+1] != number:
                result_sum += num_list[i]
        elif i == len(num_list)-1:
            if num_list[i] != number and num_list[i-1] != number:
                result_sum += num_list[i]
        else:
            if num_list[i] != number and num_list[i-1] != number and num_list[i+1] != number:
                result_sum += num_list[i]
    return result_sum


num_list = [1, 7, 3, 4, 1, 7, 10, 5]
number = 7
print(sum_of_elements(num_list, number))
