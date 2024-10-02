# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        while head:
            l += 1
            if n1.next != None:
                n1 = n1.next 
            else:
                break
        n1 = head
        if l - n == 0:
            head = head.next
            return head
        c = 0
        while n1:
            if (l - n - 1) == c:
                if n1.next and n1.next.next != None:
                    n1.next = n1.next.next
                else:
                    n1.next = None
            c += 1
            n1 = n1.next
        return head