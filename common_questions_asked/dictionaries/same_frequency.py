"""

Same Frequency

Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

Example:
    list1 = [1, 2, 3, 2, 1]
    list2 = [3, 1, 2, 1, 3]
    check_same_frequency(list1, list2)

Output: False

"""


def check_same_frequency(lst1, lst2):
    dict1, dict2 = {item1: lst1.count(item1) for item1 in lst1}, {item2: lst2.count(item2) for item2 in lst2}
    check = dict1 == dict2
    return check


if __name__ == "__main__":
    lst1, lst2 = [1, 2, 3, 2, 1], [3, 1, 2, 1, 3]
    result = check_same_frequency(lst1, lst2)
    print(result)
