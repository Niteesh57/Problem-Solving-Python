# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        r = []
        q = deque([root])
        q.append(None)
        while len(q) > 1:
            temp = q.popleft()
            if temp == None:
                r.append(None)
                q.append(None)
                continue
            else:
                r.append(temp.val)
            if temp.left != None:
                q.append(temp.left)
            if temp.right != None:
                q.append(temp.right)
        temp = []
        for i in range(1,len(r)):
            if r[i] == None:
                temp.append(r[i-1])
        if r[-1] != None:
            temp.append(r[-1])
        return temp
            