"""

Power of a number

Calculate the power of a number using recursion.

"""


def power_of_number(base_number, exponential_power):
    if not isinstance(exponential_power, int):
        raise ValueError("The exponential power should be of integer type !!!")
    elif exponential_power == 0:
        return 1
    elif exponential_power > 0:
        return base_number * power_of_number(base_number, (exponential_power - 1))
    elif exponential_power < 0:
        return 1 / base_number * power_of_number(base_number, (exponential_power + 1))


if __name__ == "__main__":
    try:
        base_number1, exponential_power1 = 5, 3
        result1 = power_of_number(base_number=base_number1, exponential_power=exponential_power1)
        print(result1)
        base_number2, exponential_power2 = -5, 3
        result2 = power_of_number(base_number=base_number2, exponential_power=exponential_power2)
        print(result2)
        base_number3, exponential_power3 = -5, 3.3
        result3 = power_of_number(base_number=base_number3, exponential_power=exponential_power3)
        print(result3)
    except Exception as e:
        print(e.__str__())
