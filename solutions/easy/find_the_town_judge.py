class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and trust == []:
            return 1
        a = set()
        b = []
        for i in trust:
            a.add(i[0])
            b.append(i[1])
            if i[0] in b:
                b.remove(i[0])
        c = Counter(b)
        if n - 1 == len(a):
            for i,j in c.items():
                if len(a) == j:
                    return i
        return -1