class Solution:
    def maximum69Number (self, num: int) -> int:
        n = int(num)
        num = list(str(num))
        for i in range(len(num)):
            if num[i] == '9':
                temp = list(num)
                temp[i] = '6'
                n = max(n,int("".join(temp)))
            else:
                temp = list(num)
                temp[i] = '9'
                n = max(n,int("".join(temp)))
        return n