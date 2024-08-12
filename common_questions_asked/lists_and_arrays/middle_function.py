"""

Middle Function

Write a function called middle that takes a list and returns a new list that contains all but the
first and last elements.

Example:
    myList = [1, 2, 3, 4]
    middle(myList)  # [2,3]

"""


def middle(lst):
    lst = lst[1:-1]
    return lst


if __name__ == "__main__":
    lst = [1, 7, 3, 4, 9, 5]
    result = middle(lst=lst)
    print(result)
