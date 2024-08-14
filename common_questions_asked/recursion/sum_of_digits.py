"""

Sum of Digits of a Positive Number

Find out the sum of a positive integer number using recursion.

"""


def sum_of_digits(number):
    if number < 0 or not isinstance(number, int):
        raise ValueError("The number should be a positive integer number.")
    elif number == 0:
        return 0
    else:
        return int(number % 10) + sum_of_digits(int(number // 10))


if __name__ == "__main__":
    try:
        number1, number2 = 1234, -1233
        result1 = sum_of_digits(number=number1)
        print(result1)
        result2 = sum_of_digits(number=number2)
        print(result2)
    except Exception as e:
        print(e.__str__())
