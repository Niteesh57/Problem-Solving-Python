class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        d = {}
        w = {}
        c = 0
        x = []
        for i in pattern:
            x = w.get(s[c])
            if i in d and d[i] == s[c]:
                d[i] = s[c]
            elif i not in d:
                if x in d:
                    return False
                d[i] = s[c]
                w[s[c]] = i
            else:
                return False
            c += 1
        return True