class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #
        #
        #
        #
        #
        # [7,1]
        # [0,0]
        #.[6,7,1]
        # [1,0,0]#
        # [5,6,7,1]
        # [2,1,0,0]
        #

        biggest = 0
        for i in range(len(prices)):
            
            for j in range(i + 1, len(prices)):

                biggest = max(biggest, prices[j] - prices[i])
        
        return biggest
