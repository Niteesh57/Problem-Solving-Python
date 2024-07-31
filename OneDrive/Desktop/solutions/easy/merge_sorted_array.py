class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            x = nums1.index(0)
            nums1[x] = nums2[i]
        nums1.sort()
        return 