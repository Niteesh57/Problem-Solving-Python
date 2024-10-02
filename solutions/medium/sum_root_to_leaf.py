# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []
        def fun(root, val):
            if root == None:
                return 
            val.append(root.val)
            if root.left is None and root.right is None:
                result.append(tuple(val[:]))
            else:
                fun(root.left, val)
                fun(root.right, val)
            val.pop() 
        fun(root,[])
        x = 0
        for i in result:
            x += int("".join(map(str,i)))
        return x