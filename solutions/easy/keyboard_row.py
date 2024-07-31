class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        x = []
        n = 0
        keyword = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        while n < len(keyword):
            for i in words:
                l = keyword[n]
                pattern = f"[{l}]"
                data = re.findall(pattern,i.lower())
                if len(data) == len(i):
                    x.append(i)
            n += 1
        return x