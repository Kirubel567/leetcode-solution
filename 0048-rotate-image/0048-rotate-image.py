class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)): 
            for j in range(i + 1, len(matrix)): #here we start from i + 1 to avoid duplication around the diagonal, we are swapping around the diagonal and we could get the values from one side to swap no need to swap two times
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)): 
            matrix[i].reverse()

       