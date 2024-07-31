import array
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        x = array.array('i',[])
        for i in nums:
            if i in x:
                return i
            x.append(i)
        return -1