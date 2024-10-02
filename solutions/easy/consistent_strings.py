class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        a = set(allowed)
        for i in words:
            if a == set(i) and len(a) == len(set(i)):
                ans += 1
            elif set(i).issubset(a) and len(a) > len(set(i)):
                ans += 1
        return ans
        