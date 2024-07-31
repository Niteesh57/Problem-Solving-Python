class Solution:
    def findLHS(self, nums: List[int]) -> int:
        x = {}
        l = 0
        l1 = []
        for i in nums:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1
        for i,j in x.items():
            print(i)
            x1 = x.get(i+1)
            if x1 != None:
                l += x1 + j
            l1.append(l)
            l = 0
        return max(l1)