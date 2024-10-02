class Solution:
    def fib(self, n: int) -> int:
        x = [0,1]
        if n > 2:
            for i in range(n):
                x.append(x[-1] + x[-2])
            return x[n]
        else:
            return 1 if n != 0 else 0