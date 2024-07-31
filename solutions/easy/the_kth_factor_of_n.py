class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        x = []
        for i in range(1,n):
            if n % i == 0:
                x.append(i)
        x.append(n)
        try:
            return x[k-1]
        except:
            return -1