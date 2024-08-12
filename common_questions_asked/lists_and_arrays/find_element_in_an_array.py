"""

Find a number in an array.

Check if an array contains a certain value or not.

Hint: Search the element in an array using algorithms. Also use numpy array.

"""

import numpy as np


def find_number(array, number):
    for i in range(len(array)):
        if array[i] == number:
            return dict(index=i, value=number)
    raise ValueError(f"The number: {number} is not present in the array.")


if __name__ == "__main__":
    try:
        array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        number1 = 14
        result1 = find_number(array=array1, number=number1)
        print(result1)
        array2, number2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 99
        result2 = find_number(array=array2, number=number2)
        print(result2)
    except Exception as e:
        print(e.__str__())
