class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        i = 0
        s = 0
        num = str(num)
        while i <= len(num) - k:
            if int(num[i:i+k]) != 0 and (int(num) % int(num[i:i+k])) == 0:
                s += 1
            i += 1
        return s