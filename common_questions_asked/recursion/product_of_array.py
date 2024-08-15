"""

Product of Array

Write a function called productOfArray which takes in an array of numbers and returns the product of them all.

Examples:
    productOfArray([1,2,3]) #6
    productOfArray([1,2,3,10]) #60

"""


def productOfArray(arr):
    arr_len = len(arr)
    if arr_len == 0:
        return 1
    else:
        return arr[0] * productOfArray(arr=arr[1:arr_len])


if __name__ == "__main__":
    array1, array2 = [1, 2, 3], [1, 2, 3, 10]
    result1 = productOfArray(arr=array1)
    print(result1)
    result2 = productOfArray(arr=array2)
    print(result2)
