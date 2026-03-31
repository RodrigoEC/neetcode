class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # What we need to do? We need to visit each land (connected 1s) and 
        # count it to get the area of that land. Once we do it to every
        # land we need to return the biggest area found

        # How should we do it? We're using dfs to go into every path that
        # is connected to the 1 we're in and keep counting it. To be sure
        # we're not recounting the same spot we're turning the visited
        # spot into 0.

        # What algorithm or structure we're using? We're using a DFS

        # What's the time complexity of this approach? This is actually O(m * n)
        # where m is the number of row and n is the number of columns in the grid


        res = 0

        def dfs(row, column):

            if (row < 0 or
                column < 0 or
                row == len(grid) or 
                column == len(grid[0]) or
                grid[row][column] == 0):
                return 0
            
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            grid[row][column] = 0
            res = 1

            for [r, c] in directions:
                res += dfs(row + r, column + c)
            
            return res


        

        for r, row in enumerate(grid):
            for c, column in enumerate(row):

                if column == 1:
                    res = max(res, dfs(r, c))
        
        return res
        