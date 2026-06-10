class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        def update_connected(row, column):

            for i in range(len(matrix)):
                if matrix[i][column] != 0:
                    matrix[i][column] = "z"
            
            for i in range(len(matrix[0])):
                if matrix[row][i] != 0:
                    matrix[row][i] = "z"
        
        for r, row in enumerate(matrix):
            for c, column in enumerate(row):

                if column == 0:
                    update_connected(r, c)

        
        for r, row in enumerate(matrix):
            for c, column in enumerate(row):
                if column == "z":
                    matrix[r][c] = 0

