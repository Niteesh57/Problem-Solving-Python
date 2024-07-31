class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = list(s)
        for i in t[::-1]:
            if i in x:
                x.remove(i)
            else:
                return i
        return -1  
        