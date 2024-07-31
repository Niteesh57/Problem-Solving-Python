class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = list(s)
        y = list(t)
        for i in x:
            try:
                y.remove(i)
            except:
                return False
        return len(y) == 0
        