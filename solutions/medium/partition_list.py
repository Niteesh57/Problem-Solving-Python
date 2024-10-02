# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        t = head
        tempHead = None
        tempTail = None
        NextIter = []
        while t:
            if t.val < x:
                if tempHead == None:
                    tempHead= ListNode(t.val)
                    tempTail = tempHead
                else:
                    l = ListNode(t.val)
                    tempTail.next = l
                    tempTail = l
            else:
                NextIter.append(t.val)
            t = t.next
        if x == 0 and NextIter == []:
            return head
        while NextIter:
            l = ListNode(NextIter[0])
            if tempTail:
                tempTail.next = l
                tempTail = l
                NextIter.pop(0)
            else:
                tempHead = l
                tempTail = l
                NextIter.pop(0)
        return tempHead