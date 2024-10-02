# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        x = set()
        t = headA
        t1 = headB
        while t:
            x.add(t)
            t = t.next
        while t1:
            if t1 in x:
                return t1
            t1 = t1.next
        return None
        