class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        d = {}
        i = 0
        m_d = float('-inf')
        while i < len(nums):
            m_d = max(nums[i],m_d)
            temp = [nums[i]]
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    temp.append(nums[j])
                else:
                    break
            if nums[i] not in d:
                d[nums[i]] = [len(temp)]
            else:
                d[nums[i]].append(len(temp))
            i += len(temp)
        return max(d.get(m_d))