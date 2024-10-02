# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        pre = None
        Next = None
        while t and t.next:
            print(t.val,t.next.val)
            if t.val % min(t.val,t.next.val) == 0 and t.next.val % min(t.val,t.next.val) == 0:
                pre = t.next
                t.next = ListNode(min(t.val,t.next.val))
                t.next.next = pre
            else:
                for i in range(min(t.val,t.next.val),0,-1):
                    if t.val % i == 0 and t.next.val % i == 0:
                        pre = t.next
                        t.next = ListNode(i)
                        t.next.next = pre
                        break
            t = t.next.next
        return head
        