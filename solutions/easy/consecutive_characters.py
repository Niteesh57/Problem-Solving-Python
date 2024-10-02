class Solution:
    def maxPower(self, s: str) -> int:
        pre = []
        i = 0
        m = 1
        while i < len(s):
            if pre == []:
                pre.append(s[i])
            elif s[i] in pre:
                pre.append(s[i])
            else:
                pre = []
                pre.append(s[i])
            m = max(m,len(pre))
            i += 1
        return m
        