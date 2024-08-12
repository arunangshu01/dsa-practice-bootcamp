"""

Insert at the Beginning

Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning
of the original tuple.

Example:
    input_tuple = (2, 3, 4)
    value_to_insert = 1
    output_tuple = insert_value_front(input_tuple, value_to_insert)
    print(output_tuple)  # Expected output: (1, 2, 3, 4)

"""


def insert_value_front(input_tuple, value_to_insert):
    single_tuple = (value_to_insert, )
    result_tuple = single_tuple + input_tuple
    return result_tuple


if __name__ == "__main__":
    input_tuple, value_to_insert = (2, 3, 4), 1
    result = insert_value_front(input_tuple=input_tuple, value_to_insert=value_to_insert)
    print(result)
