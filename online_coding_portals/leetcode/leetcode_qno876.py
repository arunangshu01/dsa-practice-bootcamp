"""

LeetCode Question: 876. Middle of the Linked List

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     length = 0
    #     start = node = head
    #     while start:
    #         length += 1
    #         start = start.next
    #     middle = length // 2
    #     i = 0
    #     while node:
    #         if i == middle:
    #             return node
    #         else:
    #             i += 1
    #             node = node.next
    #     return None
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
