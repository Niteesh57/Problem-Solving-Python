class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = []
        while (n > 0):
            i = n % 2
            x.append(i)
            n //= 2
        for i in range(len(x) - 1):
            if x[i] == x[i+1]:
                return False
        return True