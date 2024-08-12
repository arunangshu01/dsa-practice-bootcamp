"""

Concatenate

Write a function that takes a tuple of strings and concatenates them, separating each string with a space.

Example:
    input_tuple = ('Hello', 'World', 'from', 'Python')
    output_string = concatenate_strings(input_tuple)
    print(output_string)  # Expected output: 'Hello World from Python'

"""


def concatenate_strings(input_tuple):
    result_string = " ".join(input_tuple)
    return result_string


if __name__ == "__main__":
    input_tuple = ('Hello', 'World', 'from', 'Python')
    result = concatenate_strings(input_tuple)
    print(result)
