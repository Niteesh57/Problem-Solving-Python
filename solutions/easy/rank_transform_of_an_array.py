class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        l = 1
        n = []
        a = 0
        for i in sorted(arr):
            if i not in d:
                d[i] = l - a
            else:
                x = d.get(i)
                d[i] = x
                a += 1
            l += 1
        for i in arr:
            n.append(d.get(i))
        return n