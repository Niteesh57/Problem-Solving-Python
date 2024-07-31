class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = list(set(nums))
        try:
            x.sort()
            return x[::-1][2]
        except:
            return max(x)