class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        d = {}
        x = list(s)
        ans = ''
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i]
            else:
                temp = d.get(s[i])
                for j in temp:
                    temp2 = "".join(x[j:i+1])
                    if len(ans) < len(temp2) and temp2 == temp2[::-1]:
                        ans = temp2 
                d[s[i]].append(i)
        if ans == "" and len(s) > 1:
            return s[0] 
        return ans