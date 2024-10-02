class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = k % len(nums)
        x = nums[::-1][:m]
        x1 = nums[::-1][m:]
        nums[:] = x[::-1] + x1[::-1]
        return nums
        