class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if "B"*k in blocks:
            return 0
        else:
            m = 100
            for i in range(len(blocks)-k+1):
                x = blocks[i:i+k].count('B')
                m = min(m,k - x)
        return m