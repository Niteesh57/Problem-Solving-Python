class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        t = 1
        for i in sorted(arr):
            if i not in d:
                d[i] = t
                t += 1
        for i in arr:
            yield d[i] 