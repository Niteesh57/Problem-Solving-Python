class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        x = list(zip(nums,index))
        for i in x:
            result.insert(i[1],i[0])
        return result 
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.insert(index[i],nums[i])
        return result