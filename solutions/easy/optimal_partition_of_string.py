class Solution:
    def partitionString(self, s: str) -> int:
        x = []
        temp = ''
        for i in s:
            if i not in temp:
                temp += i
            else:
                x.append(temp)
                temp = i
        if len(temp) != 0:
            x.append(temp)
        return len(x)