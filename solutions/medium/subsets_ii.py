class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        def help(arrs,k):
            if k == len(nums):
                result.append(arrs[:])
                return
            arrs.append(nums[k])
            help(arrs,k+1)
            arrs.pop()
            help(arrs,k+1)
        help([],0)
        return [list(i) for i in set([tuple(sorted(i)) for i in result])]