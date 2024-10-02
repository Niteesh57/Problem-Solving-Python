class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        x = {}
        for i in range(1,10):
            temp = []
            for j in range(n+1):
                if str(i) in str(j)[0]:
                    temp.append(j)
            x[i] = temp
        l = []
        for i in x.values():
            l += i
        return l
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        x = []
        c = 1
        while len(x) < n:
            x.append(c)
            if c * 10 <= n:
                c *= 10
            else:
                while c == n or c % 10 == 9:
                    c //= 10
                c += 1
        return x