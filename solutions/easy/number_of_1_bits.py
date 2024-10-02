class Solution:
    def hammingWeight(self, n: int) -> int:
        a = 0
        while n:
            if n & 1:
                a += 1
            n = n >> 1
        return a