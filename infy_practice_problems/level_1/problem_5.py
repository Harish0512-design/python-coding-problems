# Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.
# It should return a list in which the first value should be letter count and second value should be digit count.
# Ignore the spaces or any other special character in the sentence.
import re


def count_digits_letters(sentence):
    result_list = []
    letters = (re.findall("[A-Za-z]", sentence))
    result_list.append(len(letters))
    nums = (re.findall("[0-9]", sentence))
    result_list.append(len(nums))

    return result_list


sentence = "ABC 570027"
print(count_digits_letters(sentence))
