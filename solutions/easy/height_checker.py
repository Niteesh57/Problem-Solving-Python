class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = sorted(heights)
        s = 0
        for i in range(len(temp)):
            if heights[i] != temp[i]:
                s += 1
        return s