import sys
sys.setrecursionlimit(1000)


def factorial(n):
    if n < 0 or not isinstance(n, int):
        raise ValueError("The number must be positive integer only !!!")
    elif n in [0, 1]:
        return 1
    return n * factorial(n=n - 1)


if __name__ == "__main__":
    try:
        n1, n2, n3 = 3, -1, 1.1
        result1 = factorial(n=n1)
        print(result1)
        result2 = factorial(n=n2)
        print(result2)
        # result3 = factorial(n=n3)
        # print(result3)
    except Exception as e:
        print(e.__str__())
