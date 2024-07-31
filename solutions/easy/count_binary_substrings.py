class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        con = 0
        val = 0
        index = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                index.append(1)
            else:
                print(index[-1])
                index[-1] += 1
        for i in range(len(index)-1):
            val += min(index[i+1],index[i])
        return val