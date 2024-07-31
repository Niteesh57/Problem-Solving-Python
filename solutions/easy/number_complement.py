class Solution:
    def findComplement(self, num: int) -> int:
        x = []
        value = 0
        while num > 0:
            if (num & 1):
                x.append(0)
            else:
                x.append(1)
            num = num >> 1
        x1 = 1
        for i in range(len(x)):
            value += x[i] * x1
            x1 *= 2
        return value