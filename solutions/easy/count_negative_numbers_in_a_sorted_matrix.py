class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        s = 0
        for i in grid:
            for j in i[::-1]:
                if j < 0:
                    s += 1
                else:
                    break
        return s