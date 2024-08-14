"""

Decimal to Binary

Convert a number to decimal to binary using recursion

"""


def decimal_to_binary(decimal_number):
    if not isinstance(decimal_number, int):
        raise ValueError("The number be an integer !!!")
    elif decimal_number == 0:
        return 0
    return decimal_number % 2 + 10 * decimal_to_binary(int(decimal_number / 2))


if __name__ == "__main__":
    try:
        decimal_number = 15
        result = decimal_to_binary(decimal_number=decimal_number)
        print(result)
        decimal_number2 = 1.5
        result2 = decimal_to_binary(decimal_number=decimal_number2)
        print(result2)
    except Exception as e:
        print(e.__str__())
