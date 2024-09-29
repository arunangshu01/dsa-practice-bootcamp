"""

Permutation

Check if two given two lists is permutation of each other or not.

"""


def permutation(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    lst1.sort(), lst2.sort()
    if lst1 == lst2:
        return True
    return False


if __name__ == "__main__":
    lst1, lst2 = [1, 2, 3], [1, 3, 2]
    lst3, lst4 = ['a', 'c', 'd'], ['c', 'a', 'b']
    result1 = permutation(lst1, lst2)
    result2 = permutation(lst3, lst4)
    print(result1)
    print(result2)
