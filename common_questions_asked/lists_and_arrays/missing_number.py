"""

Missing Number

Write a function to find the missing number in a given integer array of 1 to 100. The function takes to parameter the
array and the number of elements that needs to be in array. For example if we want to find missing number from 1 to 6
the second parameter will be 6.

Example: missing_number([1, 2, 3, 4, 6], 6) # 5

"""


def missing_number(arr, n):
    arr_sum = sum(arr)
    total_sum = (n * (n + 1)) / 2
    missing_num = total_sum - arr_sum
    return int(missing_num)


if __name__ == "__main__":
    arr, n = [1, 2, 3, 4, 6], 6
    result = missing_number(arr=arr, n=n)
    print(result)

