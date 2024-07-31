class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = len(nums)
        x = []
        y = []
        for i in range(len(nums)):
            if nums[i] == 0:
                x.append(i)
            else:
                y.append(i)
        c = 0
        for i in y:
            nums[c] = nums[i]
            c += 1
        x = [0]*len(x)
        nums[c:l] = x
        return nums