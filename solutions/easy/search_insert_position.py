class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            x = nums.index(target)
        except:
            x = 0
        if x:
            return x
        elif max(nums) < target:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i