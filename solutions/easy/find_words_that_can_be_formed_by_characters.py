class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        s = 0
        for i in words:
            temp = dict(Counter(chars))
            c = len(i)
            for j in i:
                t = temp.get(j)
                if t:
                    temp[j] -= 1
                    c -= 1
                else:
                    break
            if c == 0:
                s += len(i)
        return s