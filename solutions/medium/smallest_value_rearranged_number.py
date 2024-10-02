class Solution:
    def smallestNumber(self, num: int) -> int:
        x = list(str(num))
        x.sort()
        if x[0] == '0' and len(x) > 1 and num:
            for i in range(len(x)):
                if x[i] != '0':
                    temp = x[i]
                    x[i] = x[0]
                    x[0] = temp
                    break
            return int("".join(x))
        elif x[0] == '0' and len(x) <= 1:
            return int(0)
        elif x[0] != '-':
            return int("".join(x))
        else:
            x = x[::-1]
            return int('-'+"".join(x[:-1]))