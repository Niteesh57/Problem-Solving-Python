class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l = 0
        d = len(s)
        x = []
        for i in s:
            if i == 'I':
                x.append(l)
                l += 1
            else:
                x.append(d)
                d -= 1
        if s[len(s)-1] == 'I':
            x.append(l)
            l += 1
        else:
            x.append(d)
            d -= 1
        return x