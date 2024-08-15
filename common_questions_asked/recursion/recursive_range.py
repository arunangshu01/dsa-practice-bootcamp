"""

Recursive Range

Write a function called recursiveRange which accepts a number and adds up all the numbers from 0 to the number
passed to the function.

Examples:
    recursiveRange(6) # 21
    recursiveRange(10) # 55

"""


def recursiveRange(num):
    if num < 0 or not isinstance(num, int):
        raise ValueError("The number should be a positive integer !!!")
    elif num in [0, 1]:
        return num
    else:
        return num + recursiveRange(num=(num - 1))


if __name__ == "__main__":
    try:
        number1, number2, number3 = 6, 10, -4
        result1 = recursiveRange(num=number1)
        print(result1)
        result2 = recursiveRange(num=number2)
        print(result2)
        result3 = recursiveRange(num=number3)
        print(result3)
    except Exception as e:
        print(e.__str__())
