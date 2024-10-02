class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()
    def add(self, val: int) -> int:
        i = val
        l, r = 0, len(self.nums) - 1
        while l <= r:
            mid = l + (r - l) // 2  # Proper mid-point calculation

            if self.nums[mid] < i:
                l = mid + 1  # Move to the right half
            else:
                r = mid - 1  # Move to the left half
        self.nums.insert(l, i)
        return self.nums[::-1][self.k-1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)