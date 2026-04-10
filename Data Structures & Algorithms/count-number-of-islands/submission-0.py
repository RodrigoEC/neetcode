class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        


        def dfs(row, column):

            if (column < 0 or
                row < 0 or 
                column >= len(grid[0]) or
                row >= len(grid) or
                grid[row][column] != "1"):
                return

            grid[row][column] = "0"
            dfs(row, column + 1)
            dfs(row, column - 1)
            dfs(row + 1, column)
            dfs( row - 1, column)
        

        islands = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "1":
                    dfs(r, c)
                    islands += 1
        

        return islands