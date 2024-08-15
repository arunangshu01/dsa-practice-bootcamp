"""

Captalize First
Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each
string in the array.

Example:
    capitalizeFirst(['car', 'taco', 'banana']) # ['Car','Taco','Banana']

"""


def capitalizeFirst(arr):
    arr_len = len(arr)
    if arr_len == 0:
        return []
    else:
        return [arr[0].capitalize()] + capitalizeFirst(arr=arr[1:arr_len])


if __name__ == "__main__":
    array1 = ['car', 'taco', 'banana']
    result1 = capitalizeFirst(arr=array1)
    print(result1)
