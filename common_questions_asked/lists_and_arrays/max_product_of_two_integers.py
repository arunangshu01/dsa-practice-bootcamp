"""

Max Product of Two Integers

Find the maximum product of two integers in an array where all elements are positive.

Example:
    arr = [1, 7, 3, 4, 9, 5]
    max_product(arr) # Output: 63 (9*7)

"""


def max_product(arr):
    first_max, second_max = float("-inf"), float("-inf")
    for number in arr:
        if number > first_max:
            second_max = first_max
            first_max = number
        elif number > second_max:
            second_max = number
    prod = first_max * second_max
    return prod


if __name__ == "__main__":
    array = [1, 7, 3, 4, 9, 5]
    result = max_product(arr=array)
    print(result)
