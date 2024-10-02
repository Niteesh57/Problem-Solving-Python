# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempHead = None
        tempTail = None
        t = head
        dup = []
        while t:
            if t.next != None and t.val == t.next.val:
                dup.append(t.val)
            if t.val in dup:
                pass
            else:
                l = ListNode(t.val)
                if tempHead == None:
                    tempHead = l
                    tempTail = l
                else:
                    tempTail.next = l
                    tempTail = l
            t =  t.next
        return tempHead