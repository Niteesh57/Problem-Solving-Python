class Solution:
    def convertToBase7(self, num: int) -> str:
        x = []
        l = False
        data = ""
        if num < 0:
            l = True
            num = abs(num)
        if num == 0:
            return str(0)
        while num > 0:
            print(num)
            value = num % 7
            num = num // 7
            x.append(str(value))
        if l == True:
            data = "-"
        data += "".join(x[::-1])
        return data

        