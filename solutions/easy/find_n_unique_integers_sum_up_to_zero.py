class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        for i in range(1,n//2+1):
            arr.append(i)
            arr.append(-i)
        if len(arr) < n:
            arr.append(0)
        return arr