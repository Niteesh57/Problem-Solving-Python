class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        r = [0,0]
        if nums == [0,1]:
            return ["0->1"]
        if len(nums) == 1:
            return [str(nums[0])]
        nums = nums + r
        l = []
        x,y = nums[0], nums[0]
        z = 0
        while z != len(nums):
            d = y - nums[z]
            if d > 1 or d < -1:
                if x == y:
                    l.append(str(x))
                    y = nums[z]
                    x = nums[z]
                else:
                    l.append(str(x)+"->"+str(y))
                    y = nums[z]
                    x = nums[z]
            else:
                y=nums[z]
            z += 1
        return l