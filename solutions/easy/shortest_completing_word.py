import re
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        x: list = re.findall('[a-zA-Z]',licensePlate.lower())
        length = len(words) * 10
        data = ''
        for i in range(len(words)):
            li = 0
            l = list(words[i])
            for j in x:
                if j in l:
                    l.remove(j)
                    li += 1
                else:
                    break
            if len(x) == li:
                print(words[i])
                if length > len(words[i]):
                    length = len(words[i])
                    data = words[i]
        return data