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
        merged, merged_list = None, None
        if not list1:
            return list2
        if not list2:
            return list1
        if list1 and list2:
            if list1.val <= list2.val:
                merged = list1
                list1 = merged.next
            else:
                merged = list2
                list2 = merged.next
            merged_list = merged
        while list1 and list2:
            if list1.val <= list2.val:
                merged.next = list1
                merged = list1
                list1 = merged.next
            else:
                merged.next = list2
                merged = list2
                list2 = merged.next
        if not list1:
            merged.next = list2
        if not list2:
            merged.next = list1
        return merged_list
