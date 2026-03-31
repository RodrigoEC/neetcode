class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        # What we need to do?
        #
        #
        # cost = [1,2,3]
        # We need to return the smallest cost so we can reach
        # the end of the staircase. We can jump 1 or 2 steps
        # everytime.
        #
        #
        # How should we do it?
        # [1,2,3,0,0] 
        #  3,2,3
        #


        if len(cost) <= 2:
            return min(cost) 

        ith_1 = 0
        ith_2 = 0

        for i in range(len(cost) -1, -1, -1):
            ith_1, ith_2 = cost[i] + min(ith_1, ith_2), ith_1

        
        return min(ith_1, ith_2)








         