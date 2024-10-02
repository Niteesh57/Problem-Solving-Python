class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x = []
        for i in nums:
            # Insert first element into x directly
            if not x:
                x.append(i)
            else:
                # Perform binary search to find the correct position to insert i
                l, r = 0, len(x) - 1
                while l <= r:
                    mid = l + (r - l) // 2  # Proper mid-point calculation

                    if x[mid] < i:
                        l = mid + 1  # Move to the right half
                    else:
                        r = mid - 1  # Move to the left half

                # Insert element i at the correct position in sorted order
                x.insert(l, i)
        return x[::-1][k-1]