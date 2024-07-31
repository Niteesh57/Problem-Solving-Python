class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        x = 1
        y = 1
        z = 0
        n -= 1
        while n != 0:
            z = x + y
            print(z)
            y = x
            x = z
            n -= 1
        return z