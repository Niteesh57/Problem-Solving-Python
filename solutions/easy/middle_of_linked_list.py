# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        x = head
        while x:
            l += 1
            x = x.next
        new = head
        m = l // 2
        c = 0
        while new:
            if m == c:
                head = new
                return head
            c += 1
            new = new.next 