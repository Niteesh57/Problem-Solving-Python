class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        data = []
        x = {}
        for i in nums:
            if i not in x:
                x[i] = 1
            else:
                x[i] += 1
        for i,j in x.items():
            if j == 2:
                data.append(i)
                break
        val = (len(nums) * (len(nums)+1))//2
        data.append(abs(sum(x)-val))
        return data