class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        x = ""
        for i in needle:
            x += i
            if x in haystack:
                pass
            else:
                return -1
        return haystack.index(needle)