class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = []
        n = sorted(nums)
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                s.append(d.get(nums[i]))
            else:
                for j in range(len(n)):
                    if nums[i] <= n[j]:
                        s.append(j)
                        d[nums[i]] = j
                        break
        return s