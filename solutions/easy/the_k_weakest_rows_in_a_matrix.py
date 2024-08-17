class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        x = {}
        for i in range(len(mat)):
            x[i] = sum(mat[i])
        weakest_rows = sorted(x, key = lambda index : x[index])
        return weakest_rows[:k]