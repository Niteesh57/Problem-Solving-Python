class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        x = float('-inf')
        temp = 0
        for i in range(len(nums)):
            if nums[i] > x:
                x = nums[i]
                temp = i
        l = temp
        r = temp
        while l < 0 and r >= len(nums):
            l -= 1
            r += 1
            if nums[l] > x:
                return -1
            if nums[r] > x:
                return -1
        return temp