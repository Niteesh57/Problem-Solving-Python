class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = set(nums)
        y = []
        for i in range(1,len(nums)+1):
            if i not in x:
                y.append(i)
        return y
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = {}
        for i in range(1,len(nums)+1):
            x[i] = 0
        for i in nums:
            x[i] += 1
        r = []
        for i,j in x.items():
            if j == 0:
                r.append(i)
        return r
        