class Solution:
    def isHappy(self, n: int) -> bool:
        if len(str(n)) == 1 and n == 1:
            return True
        elif len(str(n)) == 1 and n != 7:
            return False
        y = 0
        for i in str(n):
            y += int(i)**2
        return Solution.isHappy(self,y)