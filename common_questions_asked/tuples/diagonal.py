"""

Diagonal

Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

Example:
    input_tuple = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    )
    output_tuple = get_diagonal(input_tuple)
    print(output_tuple)  # Expected output: (1, 5, 9)

"""


def get_diagonal(input_tuple):
    diagonal_list = []
    for i in range(len(input_tuple)):
        for j in range(len(input_tuple[i])):
            if i == j:
                diagonal_list.append(input_tuple[i][j])
    duplicate_tuple = tuple(diagonal_list)
    return duplicate_tuple


if __name__ == "__main__":
    input_tuple = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    )
    result = get_diagonal(input_tuple)
    print(result)
