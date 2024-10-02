class Solution:
    def sortString(self, s: str) -> str:
        x = []
        c = Counter(s)
        temp = sorted(set(s))
        t1 = True
        sum_all = sum(c.values())
        while  sum_all > 0:
            if t1:
                for i in temp:
                    if c.get(i):
                        x.append(i)
                        c[i] -= 1
                        sum_all -= 1
                t1 = False
            else:
                for i in temp[::-1]:
                    if c.get(i):
                        x.append(i)
                        c[i] -= 1
                        sum_all -= 1
                t1 = True
        return "".join(x)