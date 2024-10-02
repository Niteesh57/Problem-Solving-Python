class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        x = 0
        x1 = 0
        s = 1
        s1 = 1
        m = float('-inf')
        for i in range(len(nums)):
            s *= nums[i]
            x = s
            if s == 0:
                s = 1
            s1 *= nums[len(nums) - i - 1]
            x1 = s1
            if s1 == 0:
                s1 = 1
            if m < x:
                m = x
            if m < x1:
                m = x1
        return m