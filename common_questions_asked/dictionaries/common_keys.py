"""

Common Keys

Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

Example:
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    merge_dicts(dict1, dict2)

Output:
    {'a': 1, 'b': 5, 'c': 7, 'd': 5}

"""


def merge_dicts(dict1, dict2):
    for key in dict2:
        if key in dict1:
            dict1.update({key: dict1[key] + dict2[key]})
        else:
            dict1.update({key: dict2[key]})
    return dict1


if __name__ == "__main__":
    dict1, dict2 = {'a': 1, 'b': 2, 'c': 3}, {'b': 3, 'c': 4, 'd': 5}
    result = merge_dicts(dict1=dict1, dict2=dict2)
    print(result)
