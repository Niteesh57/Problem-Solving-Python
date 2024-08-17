class Solution:
    def balancedStringSplit(self, s: str) -> int:
        x = 0
        i_val = 0
        for i in range(len(s)):
            temp_r, temp_l = 0,0
            for j in range(i,len(s)):
                if s[j] == 'R':
                    temp_r += 1
                elif s[j] == 'L':
                    temp_l += 1
                if temp_l == temp_r:
                    i_val = j
            if temp_r == temp_l:
                x += 1
                i = i_val
        return x