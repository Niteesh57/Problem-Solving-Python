class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x = 0
        y = 0
        while y < len(t) and x < len(s):
            if s[x] == t[y]:
                x += 1
            y += 1
        return len(s) == x
