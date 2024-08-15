"""

Flatten

Write a recursive function called flatten which accepts an array of arrays and returns a new array with all
values flattened.

Examples:
    flatten([1, 2, 3, [4, 5]]) # [1, 2, 3, 4, 5]
    flatten([1, [2, [3, 4], [[5]]]]) # [1, 2, 3, 4, 5]
    flatten([[1], [2], [3]]) # [1, 2, 3]
    flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) # [1, 2, 3]

"""


def flatten(arr):
    flattened_arr = []
    for item in arr:
        if isinstance(item, list):
            flattened_arr.extend(flatten(arr=item))
        else:
            flattened_arr.append(item)
    return flattened_arr


if __name__ == "__main__":
    array1, array2, array3, array4 = [1, 2, 3, [4, 5]], [1, [2, [3, 4], [[5]]]], [[1], [2], [3]], [[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]
    result1 = flatten(arr=array1)
    print(result1)
    result2 = flatten(arr=array2)
    print(result2)
    result3 = flatten(arr=array3)
    print(result3)
    result4 = flatten(arr=array4)
    print(result4)

