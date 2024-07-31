class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start = 0
        val = set()
        n = []
        while start < len(s)-2:
            if s[start] == s[start + 1] == s[start + 2]:
                val.add(start)
                val.add(start + 1)
                val.add(start + 2)
            else:
                if len(val) != 0:
                    n.append([min(val),max(val)])
                    val = set()
            start += 1
        if len(val) != 0:
            n.append([min(val),max(val)])
        return n