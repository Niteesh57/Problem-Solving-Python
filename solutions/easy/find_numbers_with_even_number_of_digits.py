class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            s += 1 if len(str(i)) % 2 == 0 else 0
        return s