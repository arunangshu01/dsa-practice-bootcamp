"""

Common Elements

Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

Example:
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = (4, 5, 6, 7, 8)
    output_tuple = common_elements(tuple1, tuple2)
    print(output_tuple)  # Expected output: (4, 5)

"""


def common_elements(tuple1, tuple2):
    result_tuple = tuple(set(tuple1) & set(tuple2))
    return result_tuple


if __name__ == "__main__":
    tuple1, tuple2 = (1, 2, 3, 4, 5), (4, 5, 6, 7, 8)
    result = common_elements(tuple1, tuple2)
    print(result)
