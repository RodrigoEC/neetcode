class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #
        # We need to add the number of coins necessary to sum up to the
        # given amount 
        #  

        # We could try the brute force approach, which would be to try all
        # possiblities, in a tree like approach

        # coins = [1,5,10]
        #                             12
        #                      11     7    10
        #               
        #                 


        # Almost everytime we are faced with a DP problem that involves getting
        # a certain amount of some unity, we can use the following approach:

        # if we have amount = 12

        #       0,1,2,3,4,5,6,7,8,9,10,11,12
        # dp = [0,1,2,3,4,1,2,3,4,5, 1, 2, 3]
        #       

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0


        for i in range(1, amount + 1):

            for coin in coins:

                if (i - coin < 0): continue

                dp[i] = min(dp[i - coin] + 1, dp[i])
        
        return dp[amount] if dp[amount] != float('inf') else -1





