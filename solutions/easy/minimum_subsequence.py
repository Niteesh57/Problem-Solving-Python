class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        x = sum(nums)
        nums.sort()
        result = []
        for i in range(len(nums)-1,-1,-1):
            if sum(result) > x:
                return result
            result.append(nums[i])
            x -= nums[i]
        return result