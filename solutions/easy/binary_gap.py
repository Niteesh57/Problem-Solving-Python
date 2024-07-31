class Solution:
    def binaryGap(self, n: int) -> int:
        x = []
        l = []
        for i in range(32):
            if n & 1:
                x.append(i)
            n = n >> 1
        if len(x) < 2: return 0
        for i in range(len(x)-1):
            l.append(x[i+1] - x[i])
        return max(l)