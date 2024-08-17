class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp = len(arr)
        x = []
        for i in range(len(arr)):
            if arr[i] == 0:
                x.append(i+1)
        l = 0
        for i in x:
            arr.insert(i+l,0)
            l += 1
        arr[:] = arr[:temp]