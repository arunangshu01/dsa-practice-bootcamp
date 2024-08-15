"""

Is Palindrome

Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome (reads the
same forward and backward). Otherwise, it returns false.

Examples:
    isPalindrome('awesome') # false
    isPalindrome('foobar') # false
    isPalindrome('tacocat') # true
    isPalindrome('amanaplanacanalpanama') # true
    isPalindrome('amanaplanacanalpandemonium') # false

"""


def isPalindrome(strng):
    strng_len = len(strng)
    if strng_len == 0:
        return True
    elif strng[0] != strng[strng_len - 1]:
        return False
    else:
        return isPalindrome(strng=strng[1:(strng_len-1)])


if __name__ == "__main__":
    strng1, strng2, strng3, strng4, strng5 = "awesome", "foobar", "tacocat", "amanaplanacanalpanama", "amanaplanacanalpandemonium"
    result1 = isPalindrome(strng=strng1)
    print(result1)
    result2 = isPalindrome(strng=strng2)
    print(result2)
    result3 = isPalindrome(strng=strng3)
    print(result3)
    result4 = isPalindrome(strng=strng4)
    print(result4)
    result5 = isPalindrome(strng=strng5)
    print(result5)
