"""

Key with the Highest Value

Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

Example:
    my_dict = {'a': 5, 'b': 9, 'c': 2}
    max_value_key(my_dict)

Output: b

"""


def max_value_key(dict1):
    key_list, value_list = list(dict1.keys()), list(dict1.values())
    max_value_index = value_list.index(max(value_list))
    key = key_list[max_value_index]
    return key


if __name__ == "__main__":
    dict1 = {'a': 5, 'b': 9, 'c': 2}
    result = max_value_key(dict1=dict1)
    print(result)
