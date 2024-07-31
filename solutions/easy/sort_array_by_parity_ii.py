class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        x = []
        even = True
        odd = False
        for i in range(len(nums)):
            if even:
                for j in range(len(nums)):
                    if nums[j] % 2 == 0:
                        even = False
                        odd = True
                        x.append(nums[j])
                        nums.pop(j)
                        break
            else:
                for j in range(len(nums)):
                    if nums[j] % 2 == 1:
                        even = True
                        odd = False
                        x.append(nums[j])
                        nums.pop(j)
                        break
        return x
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        x = [0] * len(nums)
        even = 0
        odd = 1
        for i in nums:
            if i % 2 == 0:
                x[even] = i
                even += 2
            else:
                x[odd] = i
                odd += 2
        return x