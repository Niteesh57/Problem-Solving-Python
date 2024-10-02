class Solution:
    def maxScore(self, s: str) -> int:
        n = ''
        x = 0
        z = 0
        for i in range(0,len(s)):
            if s[i] == '0':
                z += 1
            n+=s[i] 
            c2 = s[i+1:].count('1')
            x = max(x,z+c2)
            if len(s[i+1:]) == 1:
                break
        return x
        