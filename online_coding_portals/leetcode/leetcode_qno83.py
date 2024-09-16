"""

LeetCode Question: 83. Remove Duplicates from Sorted List

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        current_node, previous_node = head, None
        duplicate_values = []
        while current_node:
            if current_node.val in duplicate_values:
                previous_node.next = current_node.next
                current_node.next = None
            else:
                duplicate_values.append(current_node.val)
                previous_node = current_node
            current_node = previous_node.next
        return head
