class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Create a copy of the matrix
        mat = [row[:] for row in matrix]
        m = len(matrix)  # Number of rows
        n = len(matrix[0])  # Number of columns

        # Iterate through the original matrix
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    # Set the row to zero in the original matrix
                    for k in range(n):  # Iterate over columns of row `i`
                        matrix[i][k] = 0
                    # Set the column to zero in the original matrix
                    for k in range(m):  # Iterate over rows of column `j`
                        matrix[k][j] = 0
