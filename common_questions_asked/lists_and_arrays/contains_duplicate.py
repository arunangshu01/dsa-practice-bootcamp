"""

Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.

Example:
    Input: nums = [1,2,3,1]
    Output: true

Hint: Use sets

"""


def contains_duplicate(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    if unique_nums == nums:
        return False
    return True


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    result = contains_duplicate(nums=nums)
    print(result)
