from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        rotten = []
        ones = 0
        for r, row in enumerate(grid):
            for c, column in enumerate(row):

                if column == 1:
                    ones += 1
                if column == 2:
                    grid[r][c] = 1
                    ones += 1
                    rotten.append((r, c))

        if ones == 0:
            return 0
        print(rotten)

        time = 0
        q = deque(rotten)
        print(q)
        

        while q:

            for i in range(len(q)):
                (r, c) = q.popleft()

                if (r < 0 or c < 0 or r == len(grid) or 
                c == len(grid[0]) or grid[r][c] != 1):
                    continue

                grid[r][c] = 2
                ones -= 1
                
                q.append((r + 1, c))
                q.append((r - 1, c))
                q.append((r, c + 1))
                q.append((r, c - 1))
            
            print(grid)
            time += 1

        time -= 2


        return -1 if ones != 0 else time

        

