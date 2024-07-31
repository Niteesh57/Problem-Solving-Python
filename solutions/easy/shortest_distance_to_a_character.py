class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        x = []
        lim = [s.index(c)]
        for i in range(len(list(s))):
            if s[i] == c:
                lim.append(i)
        for i in range(len(list(s))):
            a = min([abs(n-i) for n in lim])
            x.append(a)
        return x