class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        t1 = ''
        t2 = ''
        for i in s:
            if i == '#':
                t1 = t1[:len(t1) - 1]
            else:
                t1 += i
        for i in t:
            if i == '#':
                t2 = t2[:len(t2) - 1]
            else:
                t2 += i
        return t1 == t2