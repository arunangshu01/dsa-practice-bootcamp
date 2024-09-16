"""

LeetCode Question: 234. Palindrome Linked List

"""

from typing import Optional


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        current_node = head
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
            i += 1
            second = second.next
        second = reverse(second)
        while first and second:
            if first.val != second.val:
                return False
            else:
                first, second = first.next, second.next
        return True
