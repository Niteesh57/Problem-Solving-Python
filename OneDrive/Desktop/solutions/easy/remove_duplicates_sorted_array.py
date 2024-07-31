class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        l = []
        for i in nums:
            if i not in l:
                l.append(i)
                nums[x] = i
                x += 1
        return x

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[a] =  nums[i]
                a += 1
        
                
        return a
