class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        d = {}
        for i in candyType:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return min(len(candyType)//2,len(d))