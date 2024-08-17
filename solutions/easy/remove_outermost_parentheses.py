class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        temp = ''
        o = 0
        l = 0
        ans = ''
        for i in s:
            if i == '(':
                temp += i
                o += 1
            else:
                temp += i
                l += 1
            if o == l:
                o = 0
                l = 0
                xleg = len(temp)
                ans += temp[1:xleg-1]
                temp = ''
        return ans