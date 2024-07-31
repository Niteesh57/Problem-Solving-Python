class Solution:
    def arrangeCoins(self, n: int) -> int:
        for i in range(1,n+1):
            x = n-i
            if x == 0:
                return i
            if x < 0:
                return i-1
            n = n-i