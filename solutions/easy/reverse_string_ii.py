class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        x = True
        s = list(s)
        for i in range(0,len(s),k):
            if x:
                p = s[i:i+k]
                s[i:i+k] = p[::-1]
                print(p)
                x = False
            else:
                x = True
        return "".join(s)

        