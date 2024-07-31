class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            temp = min(nums)
            x = nums.index(temp)
            nums[x] = -nums[x]
        return sum(nums)