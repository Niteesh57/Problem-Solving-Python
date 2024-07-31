class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s = words[0]
        d = {}
        x = []
        for i in range(1,len(words)):
            d[i] = dict(Counter(words[i]))
        for i in s:
            count = 0
            for j in range(1,len(words)):
                temp = d[j].get(i)
                if temp:
                    d[j][i] -= 1
                    count += 1
            if count == len(words)-1:
                x.append(i)
        return x