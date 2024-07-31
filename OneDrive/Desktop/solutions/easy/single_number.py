class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        if len(nums) == 1:
            return nums[0]
        for i in nums:
            if i in d:
                count = d[i]
                count += 1
                d[i] = count
            else:
                d[i] = 1
        for key,value in d.items():
            if value == 1:
                return key
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        if len(nums) == 1:
            return nums[0]
        for i in nums:
            if i in d:
                count = d[i]
                count += 1
                d[i] = count
            else:
                d[i] = 1
        return min(d.items(), key=lambda x: x[1])[0]   