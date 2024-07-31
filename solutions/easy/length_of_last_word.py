class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(" ")
        if len(x) == 1:
            return len(x[0])
        for i in range(len(x)-1,-1,-1):
            if x[i] != "":
                return len(x[i])
        return 0