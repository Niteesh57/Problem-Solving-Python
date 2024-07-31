class Solution:
    def longestPalindrome(self, s: str) -> int:
        p = False
        d = {}
        l = []
        for i in s:
            if i in d:
                x = d[i]
                x += 1
                d[i] = x
            else:
                d[i] = 1
        for i,j in d.items():
            if j % 2 == 1:
                p = True
            j = (j //2) * 2
            l.append(j)
        if p == True:
            l.append(1)
        return sum(l)