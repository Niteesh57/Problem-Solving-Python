class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        x = 0
        for i in dominoes:
            temp = tuple(sorted(i))
            if temp in d:
                d[temp] += 1
            else:
                d[temp] = 1
        for n in d.values():
            s = n*(n-1)//2
            x += s
        return x