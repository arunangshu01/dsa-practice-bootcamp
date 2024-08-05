"""

Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
    Input: head = [1,2,2,1]
    Output: true

Example 2:
    Input: head = [1,2]
    Output: false

Constraints:
    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        current_node = head
        length = 0
        while current_node:
            length += 1
            current_node = current_node.next
        middle = length // 2

        def reverse(head):
            previous_node = None
            current_node = head
            while current_node:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
            return previous_node

        first = second = head
        i = 0
        while i < middle:
            second = second.next
            i += 1
        second = reverse(second)
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True