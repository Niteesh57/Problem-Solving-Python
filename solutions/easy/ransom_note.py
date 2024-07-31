class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = list(magazine)
        x = list(ransomNote)
        for i in magazine:
            if i in x:
                x.remove(i)
            if len(x) == 0:
                return True
        return x == 0

        