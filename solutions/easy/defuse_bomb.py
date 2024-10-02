class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        x = [0]*len(code)
        c = 0
        if k > 0:
            while c < len(code):
                temp = k
                s = c+1
                while temp != 0:
                    print(s)
                    if s >= len(code):
                        s = 0
                    x[c] += code[s]
                    s += 1
                    temp -= 1
                c += 1
            return x
        elif k < 0:
            k = abs(k)
            code = code[::-1]
            while c < len(code):
                temp = k
                s = c+1
                while temp != 0:
                    print(s)
                    if s >= len(code):
                        s = 0
                    x[c] += code[s]
                    s += 1
                    temp -= 1
                c += 1
            return x[::-1]
        else:
            return x