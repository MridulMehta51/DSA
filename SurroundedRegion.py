class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 

        height,width = len(board) , len(board[0])

        def mark(r,c):
            if 0<=r <height and 0 <=c<width and board[r][c] =="O":
                board[r][c]="C"
                mark(r-1,c)
                mark(r+1,c)
                mark(r,c+1)
                mark(r,c-1)


        for r in [0,height-1]:
            for c in range(width):
                mark(r,c)
        for c in [0,width-1]:
            for r in range(height):
                mark(r,c)

        for  r in range(height):
            for c in range(width):
                if board[r][c]=="C":
                    board[r][c]="O"
                elif board[r][c]=="O":
                    board[r][c]="X"
