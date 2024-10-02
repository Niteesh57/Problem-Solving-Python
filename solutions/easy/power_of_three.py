class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        s = 1
        l = 3
        while n >= l:
            if n == l:
                return True
            l = 3 ** s
            s += 1
        return False if n != 1 else True