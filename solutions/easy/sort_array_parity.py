class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j = []
        x = []
        for i in range(len(nums)):
            j.append(nums[i]) if nums[i] % 2 == 0 else x.append(nums[i])
        return j + x