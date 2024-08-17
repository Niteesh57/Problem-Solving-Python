class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = {}
        x = []
        for i in arr:
            temp = i
            c = 0
            while i:
                if i & 1:
                    c += 1
                i = i >> 1
            if d.get(c) is None:
                d[c] = []
            d[c].append(temp)
        for i in set(d):
            x += sorted(d.get(i))
        return x