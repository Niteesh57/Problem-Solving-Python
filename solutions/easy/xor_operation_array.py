class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        s = start
        temp = start
        while n != 1:
            s ^= temp + 2
            temp += 2
            n -= 1
        return s