"""

Pairs

Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider
commutative pairs.

Example:
    pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
    Output : ['2+5', '4+3', '3+4', '-2+9']

Note:
    4+3 comes from second and third elements from the main list.
    3+4 comes from third and seventh elements from the main list.

"""


def pair_sum(arr_list, sum_no):
    sum_pairs = []
    for i in range(len(arr_list)):
        for j in range(i + 1, len(arr_list)):
            if arr_list[i] + arr_list[j] == sum_no:
                sum_pairs.append(f"{arr_list[i]}+{arr_list[j]}")
    return sum_pairs


if __name__ == "__main__":
    arr_list, sum_no = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7
    result = pair_sum(arr_list=arr_list, sum_no=sum_no)
    print(result)
