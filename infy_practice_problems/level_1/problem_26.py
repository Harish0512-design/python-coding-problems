# Given a string, write a python function to return True if the strings "mat" and "jet" appear the same number of times in the given string, else return False.
#
# Note: Perform case insensitive string comparison wherever necessary.

# Sample Input                                Expected Output
# Jet on the Mat but mat is too long             False
# mat jet Jet Mat                                True

def check_occurence(string):
    res = False
    jet_count = string.lower().count('jet')
    mat_count = string.lower().count('mat')
    if jet_count == mat_count:
        res = True
    return res


string = "Jet on the Mat but mat is too long"
print(check_occurence(string))
