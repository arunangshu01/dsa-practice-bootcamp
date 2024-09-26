"""

LeetCode Question: 2446. Determine if Two Events Have Conflict

"""

from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1 = [int(event.replace(":", "")) for event in event1]
        event2 = [int(event.replace(":", "")) for event in event2]
        min_event1, min_event2 = min(event1), min(event2)
        if min_event1 > min_event2:
            event1, event2 = event2, event1

        if event2[0] in range(event1[0], event1[1] + 1):
            return True
        else:
            return False
