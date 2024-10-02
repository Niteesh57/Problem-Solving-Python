# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        try:
            if p.val != q.val:
                return False
        except:
            return False
        def helps(p,q):
            if p == None and q == None:
                return 
            try:
                if p.val != q.val:
                    return False
            except:
                return False
            l = helps(p.left, q.left)
            r = helps(p.right, q.right)
            if l == False or r == False:
                return False
        l = helps(p, q)
        if l == False:
            return False
        return True