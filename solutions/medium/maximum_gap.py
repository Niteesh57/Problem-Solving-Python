class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        m = float('-inf')
        if len(nums) <= 1:
            return 0
        else:
            nums.sort()
            for i in range(1,len(nums)):
                m = max(m,nums[i] - nums[i-1])
        return m