class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = []
        d = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    y = 0
                    for k in range(j,len(nums2)):
                        if nums1[i] < nums2[k] and y < nums2[k]:
                            y = nums2[k]
                            break
                    if y == 0:
                        x.append(-1)
                    else:
                        x.append(y)
        return x
        