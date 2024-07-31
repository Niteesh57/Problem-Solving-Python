class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        x = 0
        k = 0
        for i in nums:
            count = 1
            if i not in d:
                d[i] = count
            else:
                x = d[i]
                d[i] += 1
        for key,value in d.items():
            if x < value:
                k = key
                x = value
        return k
        