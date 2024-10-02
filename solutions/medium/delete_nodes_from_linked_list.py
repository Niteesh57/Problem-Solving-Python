# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        while head.val in nums:
            head = head.next
        t = head
        pre = None
        while t:
            if t.val in nums and t.next != None:
                temp = t
                while temp.next != None and temp.next.val in nums:
                    temp = temp.next
                if temp.next == None and pre != None:
                    pre.next = None
                    return head
                if temp.next == None and pre == None:
                    return []
                t.val = temp.next.val
                t.next = temp.next.next
            elif t.val in nums and t.next == None:
                if pre.next != None:
                    pre.next = None 
            pre = t
            t = t.next
        return head