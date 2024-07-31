class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        x = []
        nums.append(0)
        for i in nums:
            if i == 1:
                c += 1
            else:
                x.append(c)
                c = 0
        return max(x)