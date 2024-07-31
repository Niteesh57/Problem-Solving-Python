class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [abs(i)*abs(i) for i in nums]
        nums.sort()
        return nums