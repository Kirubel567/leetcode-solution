class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        res = [[0]*row for _ in range(col)]

        for i in range(row): 
            for j in range(col): 
                    res[j][i] = matrix[i][j]
        return res