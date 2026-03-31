class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

        # What we need to do?
        #
        # ["X","X","X","X"],
        # ["X","O","X","X"],
        # ["X","X","Y","Y"],
        # ["X","X","X","Y"]
        #
        #
        #

        def dfs(r, c):
            if (r < 0 or
                c < 0 or
                r >= len(board) or
                c >= len(board[0]) or
                board[r][c] == "X" or
                board[r][c] == "Y"
            ): return

            if (board[r][c] == "O"):
                board[r][c] = "Y"
                
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)



        for r in range(len(board)):
            dfs(r, 0)
            dfs(r, len(board[0]) - 1)
        
        for c in range(len(board[0])):
            dfs(0, c)
            dfs(len(board) - 1, c)
        

        for r, row in enumerate(board):
            for c, cell in enumerate(row):

                if cell == "O":
                    board[r][c] = "X"
                
                elif cell == "Y":
                    board[r][c] = "O"










