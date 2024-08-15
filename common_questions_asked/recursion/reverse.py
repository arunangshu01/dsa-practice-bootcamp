"""

Reverse

Write a recursive function called reverse which accepts a string and returns a new string in reverse.

Examples:
    reverse('python') # 'nohtyp'
    reverse('appmillers') # 'srellimppa'

"""


def reverse(strng):
    strng_len = len(strng)
    if strng_len == 0:
        return ''
    else:
        return strng[-1] + reverse(strng[0: (strng_len - 1)])


if __name__ == "__main__":
    strng1, strng2 = "python", "appmillers"
    result1 = reverse(strng=strng1)
    print(result1)
    result2 = reverse(strng=strng2)
    print(result2)

