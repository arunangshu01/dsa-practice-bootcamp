"""

Factorial

Write a function factorial which accepts a number and returns the factorial of that number. A factorial is the product
of an integer and all the integers below it; e.g., factorial four ( 4! ) is equal to 24, because 4 * 3 * 2 * 1
equals 24. factorial zero (0!) is always 1.

Examples:
    factorial(1) # 1
    factorial(2) # 2
    factorial(4) # 24
    factorial(7) # 5040

"""


def factorial(num):
    if num < 0 or not isinstance(num, int):
        raise ValueError("The number should be a positive integer !!!")
    elif num in [0, 1]:
        return 1
    else:
        return num * factorial(num=(num - 1))


if __name__ == "__main__":
    try:
        number1, number2, number3, number4, number5 = 1, 2, 4, 7, -1.1
        result1 = factorial(num=number1)
        print(result1)
        result2 = factorial(num=number2)
        print(result2)
        result3 = factorial(num=number3)
        print(result3)
        result4 = factorial(num=number4)
        print(result4)
        result5 = factorial(num=number5)
        print(result5)
    except Exception as e:
        print(e.__str__())
