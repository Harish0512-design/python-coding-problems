# Write a Python function which generates
# and returns a dictionary where the keys are numbers between 1 and n (both inclusive) and the values are square of keys.


def generate_dict(number):
    # start writing your code here
    new_dict = {}
    for n in range(1, number + 1):
        new_dict[n] = n * n

    return new_dict


number = 20
print(generate_dict(number))
