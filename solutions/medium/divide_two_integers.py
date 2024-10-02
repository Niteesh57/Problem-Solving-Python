class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = 2**31 - 1
        if dividend/divisor > n:
            return n
        elif dividend/divisor < -n:
            return -n-1
        else:
            return int(str(dividend/divisor).split(".")[0])