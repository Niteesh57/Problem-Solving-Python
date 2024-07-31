class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lowercase_letters = string.ascii_lowercase
        data = dict(zip(lowercase_letters, widths))
        x = []
        temp = 0
        for i in range(len(s)):
            if temp + data.get(s[i]) <= 100:
                temp += data.get(s[i])
            else:
                x.append(temp)
                temp = data.get(s[i])
        if temp != 0:
            x.append(temp)
        return [len(x),min(x)]
        