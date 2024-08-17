class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        x = []
        for i in range(1,len(nums),2):
            x += ([nums[i]]*nums[i-1])
        return x