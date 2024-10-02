# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x  = []
        temp = head
        pre = None
        while temp:
            if temp.val not in x:
                pre = temp
                x.append(temp.val)
            else:
                pre.next = temp.next
            temp = temp.next
        return head