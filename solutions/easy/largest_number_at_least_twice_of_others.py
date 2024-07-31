class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        x = max(nums)
        indexs = nums.index(x)
        for i in range(len(nums)):
            temp = 2 * nums[i]
            if x != nums[i] and x < temp:
                return -1
        return indexs