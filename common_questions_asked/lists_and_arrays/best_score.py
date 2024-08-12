"""

Best Score

Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example:
    myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
    first_second(myList) # 90 87

"""


def first_second(scores):
    first_best, second_best = float("-inf"), float("-inf")
    for score in scores:
        if score > first_best:
            second_best = first_best
            first_best = score
        elif score > second_best:
            second_best = score
    return first_best, second_best


if __name__ == "__main__":
    scores = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
    result = first_second(scores=scores)
    print(result)
