class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        x = nums[0]
        y = nums[1]
        x1 = x < y
        x2 = x > y
        temp1 = temp2 = None
        if x1:
            for i in nums:
                if x <= i:
                    x = i
                else:
                    return False
        elif x2:
            for i in nums:
                if x >= i:
                    x = i
                else:
                    return False
        else:
            for i in nums:
                if temp1 == False:
                    break
                if x <= i:
                    x = i
                else:
                    temp1 = False
            for i in nums:
                if temp2 == False:
                    break
                if x >= i:
                    x = i
                else:
                    temp2 = False
        if temp1 == False and temp2 == False:
            return False
        return True