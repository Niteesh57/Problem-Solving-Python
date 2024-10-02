class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        s = 0
        while l < r:
            if height[l] < height[r]:
                s = max(s, abs(l - r) * height[l])
                l += 1
            elif height[l] > height[r]:
                s = max(s, abs(l - r) * height[r])
                r -= 1
            else:
                s = max(s, abs(l - r) * height[l])
                l += 1
        return s