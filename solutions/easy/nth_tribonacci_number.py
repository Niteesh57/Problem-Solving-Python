class Solution:
    def tribonacci(self, n: int) -> int:
        l = [0,1,1] + [0]* (n - 2)
        if n > 2:
            for i in range(2,n+1):
                l[i] = l[i-1] + l[i-2] + l[i-3]
        else:
            return l[n]
        return l[-1]