"""

Power

Write a function called power which accepts a base and an exponent. The function should return the power of the base to
the exponent. This function should mimic the functionality of math.pow() - do not worry about negative bases and
exponents.

Examples:
    power(2,0) # 1
    power(2,2) # 4
    power(2,4) # 16

"""


def power(base, exponent):
    if not isinstance(exponent, int):
        raise ValueError("Exponent should be an integer !!!")
    elif exponent == 0:
        return 1
    elif exponent > 0:
        return base * power(base=base, exponent=(exponent - 1))
    elif exponent < 0:
        return 1 / base * power(base=base, exponent=(exponent + 1))


if __name__ == "__main__":
    try:
        base1, exponent1 = 2, 0
        result1 = power(base=base1, exponent=exponent1)
        print(result1)
        base2, exponent2 = 2, 2
        result2 = power(base=base2, exponent=exponent2)
        print(result2)
        base3, exponent3 = 2, 4
        result3 = power(base=base3, exponent=exponent3)
        print(result3)
        base4, exponent4 = 2, -3
        result4 = power(base=base4, exponent=exponent4)
        print(result4)
        base5, exponent5 = -2, -2
        result5 = power(base=base5, exponent=exponent5)
        print(result5)
        base6, exponent6 = 2, 4.5
        result6 = power(base=base6, exponent=exponent6)
        print(result6)
    except Exception as e:
        print(e.__str__())
