class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        temp = re.findall('[A-Za-z]',s)
        j = len(temp) - 1
        s1 = ""
        for i in s:
            if i.isalpha():
                s1 += temp[j]
                j -= 1
            else:
                s1 += i
        return s1