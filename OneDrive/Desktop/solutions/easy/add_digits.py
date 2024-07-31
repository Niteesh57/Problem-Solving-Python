class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        y = 0
        for i in str(num):
            y += int(i)
        return Solution.addDigits(self,y)