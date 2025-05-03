class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # m=len(board[0])
        # print(m)
        # mn=[[]]

        rows = len(board)
        cols = len(board[0])
        
        # Create a new matrix of same size filled with 0
        mn = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(len(board)):
            for j in range(len(board[0])):

                ele=[i,j]
                # print(ele)
                count=0
                for k in range(max(0,i-1),min(len(board),i+2)):
                    for m in range(max(0,j-1),min(len(board[0]),j+2)):
                        if (k,m)!=(i,j):
                            # print(k,m)
                            if board[k][m]==1:
                                count+=1
                if board[i][j]==1 and (count==2 or count==3):
                    mn[i][j]=1
                elif board[i][j]==0 and count==3:
                    mn[i][j]=1
        print(mn)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = mn[i][j]



