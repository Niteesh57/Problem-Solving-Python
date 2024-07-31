class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = 0
        y = len(nums)
        for i in nums:
            x += 1
            for j in range(x,y):
                sum = i + nums[j]
                if sum == target:
                    i = nums.index(i)
                    return [i,j]
                    break
