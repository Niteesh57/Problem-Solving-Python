class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        c = 0
        for i in range(left,right+1):
            val = 0
            while i:
                if i & 1:
                    val += 1
                i = i >> 1
            if val > 1:
                for i in range(2, (val//2)+1):
                    if val % i == 0:
                        break
                else:
                    c += 1
        return c