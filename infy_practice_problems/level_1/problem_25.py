# Write a python function that accepts a list of words and returns the list of integers representing the length of the corresponding words.


def list_of_count(word_list):
    count_list = []
    for word in word_list:
        count_list.append(len(word))

    return count_list


word_list = ["COme", "here"]
print(list_of_count(word_list))