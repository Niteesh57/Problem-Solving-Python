class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            x = target - numbers[i]
            if x in numbers:
                l = i+1
                r = len(numbers) - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    if numbers[mid] == x:
                        return [i+1,mid+1]
                    elif numbers[mid] < x:
                        l = mid + 1
                    else:
                        r = mid - 1
        return [-1,-1]
        