class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        m = []
        s = 'balloon'
        x1 = dict(Counter(s))
        x2 = dict(Counter(text))
        for a,b in x1.items():
            temp = x2.get(a)
            if temp == None:
                return 0
            x = floor(temp/b)
            if x == 0:
                return 0
            m.append(x)
        return min(m)