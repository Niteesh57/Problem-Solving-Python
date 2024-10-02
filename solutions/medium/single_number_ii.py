class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return min(Counter(nums), key=Counter(nums).get)
        