"""

Pairs / Two Sum

Write a program to find all pairs of integers whose sum is equal to a given number. Find the results based on both the
following protocols -

    1. Each input would have exactly one solution, and you may not use the same element twice.
    2. Each input can have more than one solution.

Example:
    Input:  lst: [2, 6, 3, 9, 11]
            sum: 9

    Output: [6, 3]

Consider the following scenarios as well -
    1. Pairs have to be distinct, i.e. (2, 2) or (3, 3) is not a valid pair.
    2. Pairs does not have to be distinct.

"""


def two_sum_find_pairs_distinct(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                pairs.append((i, j))
    return pairs


def two_sum_find_pairs_non_distinct(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((i, j))
    return pairs


def two_sum_find_pairs_distinct_new(nums, target):
    seen, pairs = {}, []
    for i, num in enumerate(nums):
        complement = target - num
        if complement == num:
            continue
        elif complement in seen:
            pairs.append((seen[complement], i))
        else:
            seen[num] = i
    return pairs


def two_sum_find_pairs_non_distinct_new(nums, target):
    seen, pairs = {}, []
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            pairs.append((seen[complement], i))
        else:
            seen[num] = i
    return pairs


if __name__ == "__main__":
    nums, target = [1, 2, 3, 2, 3, 4, 5, 6], 6
    result1 = two_sum_find_pairs_distinct(nums=nums, target=target)
    result2 = two_sum_find_pairs_non_distinct(nums=nums, target=target)
    result3 = two_sum_find_pairs_distinct_new(nums=nums, target=target)
    result4 = two_sum_find_pairs_non_distinct_new(nums=nums, target=target)
    print(result1)
    print(result2)
    print(result3)
    print(result4)
