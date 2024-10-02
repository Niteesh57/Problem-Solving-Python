class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = []
        t = []
        for i in range(len(matrix[0])):
            temp = 0
            for j in range(len(matrix)):
                temp = max(temp,matrix[j][i])
            m.append(temp)
        for i in matrix:
            t.append(min(i))
        return set(m) & set(t)