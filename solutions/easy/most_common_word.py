class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
            result = re.split(r'[ ,;.!?\';]+',paragraph.lower())
            c = Counter(result)
            c = sorted(c.items(),key=lambda x:x[1],reverse=True)
            for i in c:
                if i[0] in banned:
                    pass
                else:
                    if len(i[0]) != 0:
                        return i[0]