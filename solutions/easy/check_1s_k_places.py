class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        l = None
        for i, j in enumerate(nums):
            if l is not None and j == 1 and i - l <= k: 
                return False
            if j == 1:
                if l and i - l <= k:
                    return False
                l = i
        return True