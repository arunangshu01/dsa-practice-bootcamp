"""

Greatest Common Divisor of two numbers

Find the GCD (Greatest Common Divisor) of two numbers using recursion.

"""


def gcd_of_two_numbers(number1, number2):
    if not isinstance(number1, int):
        raise ValueError("The first number should be an integer !!!")
    elif not isinstance(number2, int):
        raise ValueError("The second number should be an integer !!!")
    elif number1 < 0:
        number1 = -1 * number1
    elif number2 < 0:
        number2 = -1 * number2
    elif number1 == 0:
        return number2
    elif number2 == 0:
        return number1
    return gcd_of_two_numbers(number2, number1 % number2)


if __name__ == "__main__":
    try:
        number1, number2 = 48, 18
        result1 = gcd_of_two_numbers(number1=number1, number2=number2)
        print(result1)
        number3, number4 = 48, -18
        result2 = gcd_of_two_numbers(number1=number3, number2=number4)
        print(result2)
        number5, number6 = 48, 1.8
        result3 = gcd_of_two_numbers(number1=number5, number2=number6)
        print(result3)
    except Exception as e:
        print(e.__str__())
