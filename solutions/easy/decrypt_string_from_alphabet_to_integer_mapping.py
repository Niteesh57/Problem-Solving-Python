class Solution:
    def freqAlphabets(self, s: str) -> str:
        d = {}
        h = []
        n = ""
        x = string.ascii_lowercase
        for i in range(1,9+1):
            d[i] = x[i-1]
        for i in range(10,27):
            d[i] = x[i-1]
        for i in s:
            if i == "#":
                n = n[:len(n)-2]
                n += d.get(int(str(h[-2]) + str(h[-1])))
                h = h[:len(h)-2]
            else:
                if i == '0':
                    h.append(i)
                    n += "0"
                else:
                    n += d.get(int(i))
                    h.append(i)
        return n