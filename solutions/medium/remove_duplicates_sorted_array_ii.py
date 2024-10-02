class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = []
        s = {}
        for i in nums:
            if i not in s:
                s[i] = 1
                l.append(i)
            else:
                s[i] += 1
                if s[i] < 3:
                    l.append(i)
        nums[:] = l
        return len(l)