def fibonacci(n):
    if n < 0 or not isinstance(n, int):
        raise ValueError("Fibonacci number should be a positive integer !!!")
    elif n in [0, 1]:
        return n
    return fibonacci(n=(n - 1)) + fibonacci(n=(n - 2))


if __name__ == "__main__":
    try:
        n1, n2, n3 = 6, -1, 1.1
        result1 = fibonacci(n=n1)
        print(result1)
        result2 = fibonacci(n=n2)
        print(result2)
        # result3 = fibonacci(n=n3)
        # print(result3)
    except Exception as e:
        print(e.__str__())
