class Solution:
    def countSegments(self, s: str) -> int:
        c = 0
        for i in s.split(" "):
            if i == "":
                pass
            else:
                c += 1
        return c