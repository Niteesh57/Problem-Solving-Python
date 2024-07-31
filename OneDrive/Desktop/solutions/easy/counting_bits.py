class Solution:
    def countBits(self, n: int) -> List[int]:
        z = n+1
        a = [0]*z
        for i in range(0,n+1):
            x = i
            count_bits = 0
            while x > 0:
                if (x&1) == 1:
                    count_bits += 1
                x = x >> 1
            a[i] = count_bits
        return a