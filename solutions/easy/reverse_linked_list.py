# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        pre = None
        while t:
            next = t.next
            t.next = pre
            pre = t
            t = next
        head = pre
        return head