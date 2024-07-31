class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        x = Counter(s1.split(" "))
        x += Counter(s2.split(" "))
        return [words[0] for words in x.items() if words[1] == 1]