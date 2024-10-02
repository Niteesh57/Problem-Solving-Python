# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        d = {}
        while t:
            if t not in d:
                d[t] = 1
            else:
                return t
            t = t.next
        return None