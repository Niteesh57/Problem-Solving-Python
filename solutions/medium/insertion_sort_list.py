# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = []
        while head:
            d.append(head.val)
            head = head.next
        l = None
        ll = None
        d.sort()
        while d:
            if l == None:
                l = ListNode(d[0])
                d.pop(0)
                ll = l
            else:
                t = ListNode(d[0])
                ll.next = t
                d.pop(0)
                ll = t
        return l