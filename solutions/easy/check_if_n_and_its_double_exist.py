class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        x = [0] * len(arr)
        for i in range(len(arr)):
            x[:] = arr
            x.pop(i)
            if 2 * arr[i] in x:
                return True
        return False