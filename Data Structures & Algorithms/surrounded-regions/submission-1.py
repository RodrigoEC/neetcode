class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # What I need to do? Change to X all the Os that are not connected to an X
        # that's on the border of the board

        # How should I do that? I could visit beforehand all the Os that are
        # on the verge of the board and make a DFS on them to select all Os
        # that should no be turned into Xs

        # What should I use? I should use either DFS or BFS to find these spots.
        # I think I'm going to use BFS just for practicing

        
        visited = set()


        def BFS(row, column):


            q = deque([[row, column]])

            while q:

                for _ in range(len(q)):

                    [r, c] = q.popleft()

                    if (r < 0 or
                        c < 0 or
                        r >= len(board) or
                        c >= len(board[0]) or
                        (r,c) in visited or 
                        board[r][c] == "X"):
                        continue
                    
                    visited.add((r,c))

                    q.append([r + 1, c])
                    q.append([r - 1, c])
                    q.append([r, c + 1])
                    q.append([r, c - 1])
        
        for r in range(len(board)):
            
            if (board[r][0] == "O"):
                BFS(r, 0)
            
            if (board[r][-1] == "O"):
                print(visited, r, len(board) - 1)
                BFS(r, len(board[0]) - 1)
        
        for c in range(len(board[0])):
            
            if (board[0][c] == "O"):
                BFS(0, c)
            
            if (board[-1][c] == "O"):
                BFS(len(board) - 1, c)
        
        print(visited)


        for r, row in enumerate(board):
            for c, column in enumerate(row):

                if (column == "O" and (r, c) not in visited):
                    board[r][c] = "X"



