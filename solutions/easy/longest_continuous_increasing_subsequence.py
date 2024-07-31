class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        x = l = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: l = i
            x = max(x,i-l+1)
        return x