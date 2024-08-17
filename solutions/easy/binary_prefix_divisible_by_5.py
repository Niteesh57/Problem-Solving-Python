class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        sums = 0
        x = []
        for i in nums:
            sums = (sums * 2 + i) % 5
            x.append(sums == 0)
        return x