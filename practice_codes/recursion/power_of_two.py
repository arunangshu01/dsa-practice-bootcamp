def power_of_two(n):
    if n == 0:
        return 1
    else:
        power = power_of_two(n - 1)
        return power * 2


if __name__ == "__main__":
    n = 4
    result = power_of_two(n=n)
    print(result)
