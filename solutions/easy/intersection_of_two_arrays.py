class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        data = set()
        x = min(len(nums1),len(nums2))
        y = 0
        if x == len(nums1):
            y = len(nums1)
            for i in range(y):
                if nums1[i] in nums2:
                    data.add(nums1[i])
        else:
            y = len(nums2)
            for i in range(y):
                if nums2[i] in nums1:
                    data.add(nums2[i])
        return list(data)
        