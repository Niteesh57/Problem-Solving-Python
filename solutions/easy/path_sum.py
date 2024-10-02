# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root.val == targetSum
        r = targetSum - root.val
        return (self.hasPathSum(root.left,r)) or (self.hasPathSum(root.right,r))