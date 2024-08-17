class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        l = 1
        while '0' in str(n-l) or '0' in str(l):
            l += 1
        return [l,n-l]