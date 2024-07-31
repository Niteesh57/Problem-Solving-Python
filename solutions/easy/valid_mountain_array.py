class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        x = 0
        y = 0
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                y += 1
            else:
                break
        for j in range(i,len(arr)-1):
            if arr[j] > arr[j+1]:
                x += 1
            else:
                return False
        if x == len(arr) - 1 or y == len(arr) - 1:
            return False
        return True