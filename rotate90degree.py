class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        mat=[[0] *n for i in range(n)]

        for  i in range(len(matrix[0])):
            for j in range(len(matrix)):
                mat[j][n-1-i]=matrix[i][j]
        for  i in range(len(matrix[0])):
            for j in range(len(matrix)):
                matrix[i][j]=mat[i][j]

          
