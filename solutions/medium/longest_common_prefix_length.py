class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = sorted(set([str(i) for i in arr1]))
        arr2 = sorted(set([str(i) for i in arr2]))
        s = 0
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            common_prefix_length = self.get_common_prefix_length(arr1[i], arr2[j])
            s = max(s, common_prefix_length)
            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
                
        return s

    def get_common_prefix_length(self, s1: str, s2: str) -> int:
        common_length = 0
        for a, b in zip(s1, s2):
            if a == b:
                common_length += 1
            else:
                break
        return common_length