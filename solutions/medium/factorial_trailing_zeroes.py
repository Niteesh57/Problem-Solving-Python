class Solution:
    def trailingZeroes(self, n: int) -> int:
        s = 0
        while n >= 5:
            n //= 5
            s += n
        return s