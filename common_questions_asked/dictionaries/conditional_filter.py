"""

Conditional Filter

Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.

Example:
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)

Output: {'b': 2, 'd': 4}

"""


def filtered_dict(dict1, condition):
    dict1 = {key: value for key, value in dict1.items() if condition(key, value)}
    return dict1


if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    condition = lambda k, v: v % 2 == 0
    result = filtered_dict(dict1=dict1, condition=condition)
    print(result)
