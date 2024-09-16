"""

LeetCode Question: 21. Merge Two Sorted Lists

"""


from typing import Optional


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_1 = []
        final_list_node = None
        while list1 is not None:
            list_1.append(list1.val)
            list1 = list1.next
        while list2 is not None:
            list_1.append(list2.val)
            list2 = list2.next
        list_1.sort(reverse=True)
        for item in list_1:
            final_list_node = ListNode(item, final_list_node)
        return final_list_node
