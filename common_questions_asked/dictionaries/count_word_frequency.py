"""

Count Word Frequency

Define a function to count the frequency of words in a given list of words.

Example:
    words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
    count_word_frequency(words)

Output:
    {'apple': 3, 'orange': 2, 'banana': 1}

"""


def count_word_frequency(words):
    word_count = {item: words.count(item) for item in words}
    return word_count


if __name__ == "__main__":
    words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
    result = count_word_frequency(words=words)
    print(result)
