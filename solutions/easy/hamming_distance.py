class Solution:
    def ind(self,n):
        b = ""
        while n > 0:
            if (n & 1):
                b += "1"
            else:
                b += "0"
            n = n >> 1
        return b
    def hammingDistance(self, x: int, y: int) -> int:
        x1 = Solution.ind(self,x)
        y1 = Solution.ind(self,y)
        data = 0
        l = max(len(x1),len(y1))
        if len(x1) < l:
            a = l - len(x1)
            x1 += "0"*a
        if len(y1) < l:
            a = l - len(y1)
            y1 += "0"*a
        l -= 1
        while l >= 0:
            if x1[l] != y1[l]:
                data += 1
            l -= 1
        return data

        