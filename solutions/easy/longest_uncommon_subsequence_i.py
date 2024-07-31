class Solution:
    def eva(self,a,b):
        l = r = 0
        val = 0
        while l < len(a) and r < len(b):
            if a[l] == b[r]:
                val += 1
            l += 1
            r += 1
        if val == 0:
            return -1
        return val 
    def findLUSlength(self, a: str, b: str) -> int:
        x = Solution.eva(self,a,b)
        if x == -1:
            if len(a) <= len(b):
                return len(b)
            elif len(b) < len(a):
                return len(a)
        else:
            if x == len(a) and x == len(b):
                return -1
            if len(a) <= len(b) and x < len(b):
                return len(b)
            elif len(b) < len(a) and x < len(a):
                return len(a)
        return x
            


        