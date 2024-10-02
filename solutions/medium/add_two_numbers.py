# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = []
        y = []
        while l1 or l2:
            if l1 != None:
                x.append(str(l1.val))
                l1 = l1.next
            if l2 != None:
                y.append(str(l2.val))
                l2 = l2.next
        temp_x = "".join(x[:])
        temp_y = "".join(y[:])
        t_1 = int(temp_x[::-1])
        t_2 = int(temp_y[::-1])
        data = str(t_1 + t_2)
        temp = None
        tail = None
        for i in data[::-1]:
            l = ListNode(i)
            if temp == None:
                temp = l
                tail = temp
            else:
                tail.next = l
                tail = l
        return temp