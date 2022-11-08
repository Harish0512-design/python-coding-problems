# Write a python function to add 'ing' at the end of a given string and return the new string.
# If the given string already ends with 'ing' then add 'ly'.
# If the length of the given string is less than 3, leave it unchanged.


def add_string(string_value):
    # start writing your code here
    if len(string_value) < 3:
        pass
    elif string_value.endswith('ing'):
        string_value+='ly'
    else:
        string_value+='ing'

    return string_value


str1 = "com"
print(add_string(str1))
