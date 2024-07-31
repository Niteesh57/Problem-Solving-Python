class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        x = []
        s = 0
        while n != 0:
            if n & 1:
                x.append(0)
            else:
                x.append(1)
            n = n >> 1
        for i in range(len(x)):
            if x[i]:
                s += 2**i
        return s