"""

Reverse Key-Value Pairs

Define a function which takes as a parameter dictionary and returns a dictionary in which the key-value pairs
are reversed.

Example:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    reverse_dict(my_dict)

Output: {1: 'a', 2: 'b', 3: 'c'}

"""


def reverse_dict(dict1):
    dict1 = {value: key for key, value in dict1.items()}
    return dict1


if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    result = reverse_dict(dict1=dict1)
    print(result)
