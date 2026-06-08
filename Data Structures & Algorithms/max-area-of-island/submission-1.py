class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        




        def dfs(row: int, column: int):
            if (row < 0 or
            row == len(grid) or
            column < 0 or
            column == len(grid[0]) or
            grid[row][column] == 0):
                return 0

            grid[row][column] = 0

            left = dfs(row, column - 1)
            right = dfs(row, column + 1)
            up = dfs(row + 1, column)
            down = dfs(row - 1, column)

            return 1 + left + right + up + down

        max_area = 0
        for r, row in enumerate(grid):
            for c, column in enumerate(row):

                if column == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area

            


            
