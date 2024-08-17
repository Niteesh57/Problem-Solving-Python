class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr = arr 
        m = -1
        for i in range(len(arr)-1,-1,-1):
            if arr[i] > m:
                temp = m
                m = arr[i]
                arr[i] = temp
            else:
                arr[i] = m
        return arr