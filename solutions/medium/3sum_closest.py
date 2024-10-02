class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        dif = float('inf')
        val = None
        for i in range(len(nums)-2):
            l = i + 1 
            r = len(nums) - 1
            while l < r:
                x = nums[i] + nums[l] + nums[r]
                if dif > abs(x - target):
                    dif = abs(x - target)
                    val = x
                if x == target:
                    return target
                elif x < target:
                    l += 1
                else:
                    r -= 1
        return val