class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        x = []
        for i in range(len(matrix[0])):
            l = i
            val = []
            for j in range(len(matrix)):
                val.append(matrix[j][l])
            x.append(val)
        return x