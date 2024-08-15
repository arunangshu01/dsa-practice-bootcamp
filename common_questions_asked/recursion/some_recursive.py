"""

Some Recursive

Write a recursive function called someRecursive which accepts an array and a callback. The function returns true if a
single value in the array returns true when passed to the callback. Otherwise it returns false.

Examples:
    someRecursive([1,2,3,4], isOdd) # true
    someRecursive([4,6,8,9], isOdd) # true
    someRecursive([4,6,8], isOdd) # false

"""


def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def someRecursive(arr, cb):
    arr_len = len(arr)
    if arr_len == 0:
        return False
    else:
        return bool(cb(arr[0]) + someRecursive(arr=arr[1:arr_len], cb=cb))


if __name__ == "__main__":
    array1, array2, array3 = [1, 2, 3, 4], [4, 6, 8, 9], [4, 6, 8]
    result1 = someRecursive(arr=array1, cb=isOdd)
    print(result1)
    result2 = someRecursive(arr=array2, cb=isOdd)
    print(result2)
    result3 = someRecursive(arr=array3, cb=isOdd)
    print(result3)
