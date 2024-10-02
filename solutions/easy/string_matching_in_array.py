class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        x = []
        temp = []
        for i in words:
            temp[:] = words
            temp.remove(i)
            for j in temp:
                if i in j and i not in x:
                    x.append(i)
        return x