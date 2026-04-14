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

        max_sell = 0
        min_val = prices[0]

        for price in prices:
            max_sell = max(max_sell, price - min_val)
            min_val = min(min_val, price)
        
        return max_sell
