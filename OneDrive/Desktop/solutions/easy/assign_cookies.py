class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        x = g
        y = s
        c = 0
        for i in x:
            for j in y:
                if i <= j:
                    y.remove(j)
                    c += 1
                    break
        return c