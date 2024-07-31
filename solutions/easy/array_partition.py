class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        val = 0
        indexs = 0
        nums.sort()
        for i in range(2,len(nums)+1,2):
            val += min(nums[indexs:i])
            indexs = i
        return val

        