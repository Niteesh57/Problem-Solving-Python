class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m = -1
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i,j in d.items():
            if i == j and i > m:
                m = i
        return m if m != -1 else -1