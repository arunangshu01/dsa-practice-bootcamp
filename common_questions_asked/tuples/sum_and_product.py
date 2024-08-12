"""

Sum and Product

Write a function that calculates the sum and product of all elements in a tuple of numbers.

Example:
    input_tuple = (1, 2, 3, 4)
    sum_result, product_result = sum_product(input_tuple)
    print(sum_result, product_result)  # Expected output: 10, 24

"""


def sum_product(input_tuple):
    sum, product = 0, 1
    for item in input_tuple:
        sum += item
        product *= item
    return sum, product


if __name__ == "__main__":
    input_tuple = (1, 2, 3, 4)
    sum_result, product_result = sum_product(input_tuple=input_tuple)
    print(sum_result, product_result)
