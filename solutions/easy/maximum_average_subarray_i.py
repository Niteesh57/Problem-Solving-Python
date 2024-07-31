class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_sum = 0
        max_avg = 0
        max_sum = sum(nums[:k])
        max_avg = max_sum/k
        for i in range(k,n):
            max_sum += nums[i]
            max_sum -= nums[i-k]
            avg = max_sum/k
            max_avg = max(max_avg,avg)
        return max_avg