# Write a python function which accepts a sentence and
# returns a list in which first value is the count of upper case letters and second value
# is the count of lower case letters in the sentence. Ignore spaces, numbers and other special characters if any.

import re


def find_upper_and_lower(sentence):
    result_list = []
    upper_cases = re.findall('[A-Z]', sentence)
    lower_cases = re.findall('[a-z]', sentence)
    result_list.append(len(upper_cases))
    result_list.append(len(lower_cases))
    return result_list


sentence = "Come Here"
print(find_upper_and_lower(sentence))
