"""

Fib

Write a recursive function called fib which accepts a number and returns the nth number in the Fibonacci sequence.
Recall that the Fibonacci sequence is the sequence of whole numbers 0,1, 1, 2, 3, 5, 8, ... which starts with 0 and 1,
and where every number thereafter is equal to the sum of the previous two numbers.

Examples:
    fib(4) # 3
    fib(10) # 55
    fib(28) # 317811
    fib(35) # 9227465

"""


def fib(num):
    if num < 0 or not isinstance(num, int):
        raise ValueError("The number should be a positive integer !!!")
    elif num in [0, 1]:
        return num
    else:
        return fib(num=(num - 1)) + fib(num=(num - 2))


if __name__ == "__main__":
    try:
        number1, number2, number3, number4, number5 = 4, 10, 28, 35, -3.4
        result1 = fib(num=number1)
        print(result1)
        result2 = fib(num=number2)
        print(result2)
        result3 = fib(num=number3)
        print(result3)
        result4 = fib(num=number4)
        print(result4)
        result5 = fib(num=number5)
        print(result5)
    except Exception as e:
        print(e.__str__())
