"""

Capitalize Words

Write a recursive function called capitalizeWords. Given an array of words, return a new array containing each word
capitalized.

Examples:
    words = ['i', 'am', 'learning', 'recursion']
    capitalizeWords(words) # ['I', 'AM', 'LEARNING', 'RECURSION']

"""


def capitalizeWords(arr):
    arr_len = len(arr)
    if arr_len == 0:
        return []
    else:
        return [arr[0].upper()] + capitalizeWords(arr=arr[1:arr_len])


if __name__ == "__main__":
    array1 = ['i', 'am', 'learning', 'recursion']
    result1 = capitalizeWords(arr=array1)
    print(result1)
