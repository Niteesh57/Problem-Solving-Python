class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        for i in range(len(s)):
            if i < len(s) - 1:
                s[i] = s[i][::-1] + " "
            else:
                s[i] = s[i][::-1]
        return "".join(s)