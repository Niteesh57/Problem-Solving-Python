class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        while start or goal:
            if (start & 1) != (goal & 1):
                ans += 1
            start = start >> 1
            goal = goal >> 1
        return ans
        