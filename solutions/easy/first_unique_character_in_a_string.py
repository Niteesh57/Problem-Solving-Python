class Solution:
    def firstUniqChar(self, s: str) -> int:
        data = {}
        for i in range(len(s)):
            if s[i] not in s[i+1::]:
                if data.count(s[i]) > 1:
                    pass
                else:
                    return i
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        data = {}
        for i in s:
            if i in data:
                x = data[i]
                x += 1
                data[i] = x
            else:
                data[i] = 1
        for i,j in data.items():
            if j == 1:
                return s.index(i)
        return -1
            