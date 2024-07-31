import math
class Solution:
    def mySqrt(self, x: int) -> int:
        y = math.sqrt(x)
        return math.floor(y)