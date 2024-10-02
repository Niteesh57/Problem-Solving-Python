class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s = 0
        e = len(nums) - 1
        if len(nums) < 2:
            if len(nums) == 1:
                return [0,0] if nums[0] == target else [-1,-1]
            return [-1,-1]
        while s <= e:
            mid  = s + (e - s) // 2
            if nums[mid] == target:
                while mid+1 <= len(nums) - 1 and nums[mid + 1] == target:
                    mid += 1
                temp = mid
                while temp-1 <= len(nums) - 1 and temp-1 >= 0 and nums[temp - 1] == target:
                    print(temp,mid)
                    temp -= 1
                return [temp,mid] if nums[mid-1] == nums[mid] else [mid,mid] 
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        return [-1,-1]