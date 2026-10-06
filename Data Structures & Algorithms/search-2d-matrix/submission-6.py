class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #
        # I know this a binary search problem.

        # target = 4
        # matrix = 
        # [[ 1, 2, 4, 8],
        #  [10,11,12,13], 
        #. [14,20,30,40]]
        #
        #
        # 


        lr, rr, mr = 0, len(matrix) - 1, len(matrix) // 2
        while lr < rr:

            middle_row = matrix[mr]
            
            if middle_row[0] <= target <= middle_row[-1]:
                break
            elif target > middle_row[-1]:
                lr = mr + 1
            else:
                rr = mr - 1
            
            mr = (lr + rr) // 2
        print(lr, mr, rr)
        l, m, r = 0, len(matrix[0]) // 2, len(matrix[0]) - 1
        sel_row = matrix[mr]
        while l <= r:

            if sel_row[m] == target:
                return True
            elif target > sel_row[m]:
                l = m + 1
            else:
                r = m - 1

            m = (r + l) // 2
        
        return sel_row[m] == target


            







