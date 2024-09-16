"""

LeetCode Question: 203. Remove Linked List Elements

"""


from typing import Optional


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        dummy_node.next = head
        previous_node, current_node = dummy_node, head
        while current_node:
            if current_node.val == val:
                previous_node.next = current_node.next
            else:
                previous_node = current_node
            current_node = current_node.next
        return dummy_node.next
