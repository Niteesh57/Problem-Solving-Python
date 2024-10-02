# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val == val:
            head = head.next
        x = head
        pre = None
        while x:
            if x.val == val:
                pre.next = x.next
            else:
                pre = x
            x = x.next
        return head    