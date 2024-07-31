class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c = 0
        l = 0
        while l < len(strs[0]):
            m = 0
            for i in strs:
                if m == 0:
                    m = ord(i[l])
                else:
                    if m > ord(i[l]):
                        c += 1
                        break
                    else:
                        m = ord(i[l])
            l += 1
        return c