class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def help(nums, n, arr):
            if n == len(nums):
                result.append(arr[:])
                return
            arr.append(nums[n])
            help(nums, n + 1, arr)
            arr.pop()
            help(nums, n+1, arr)
            return
        help(nums, 0, [])
        return result