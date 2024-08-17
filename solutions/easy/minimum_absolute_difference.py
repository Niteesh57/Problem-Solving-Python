class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        x = sorted(arr)
        t = dict()
        for i in range(len(x) - 1):
            t[tuple([x[i],x[i+1]])] = abs(x[i] - x[i+1])
        l = []
        temp = min(t.values())
        for i,j in t.items():
            if j == temp:
                l.append(list(i))
        return l