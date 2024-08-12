"""

Duplicate Number

Write a function to remove the duplicate numbers on given integer array/list.

Example:
    remove_duplicates([1, 1, 2, 2, 3, 4, 5])
    Output : [1, 2, 3, 4, 5]

"""


def remove_duplicates(arr_list):
    unique_list = []
    for item in arr_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


if __name__ == "__main__":
    arr_list = [1, 1, 2, 2, 3, 4, 5]
    result = remove_duplicates(arr_list=arr_list)
    print(result)
