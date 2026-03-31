class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        # We need to find the biggest product for a subarray of the
        # given array

        # -> The biggest product could be the product of all numbers
        # but if we have negative numbers we could actually get a smaller
        # product than a product of some subarrays


        # Things to keep an eye on
        # -> We need to store both maxProduct an minProduct, because even if
        # we get a product that's negative, if at some point we find other negatie
        # number, then we'll have a positive product!

        # ->

        # [1,2,-3,4]
        # [2,-4,-3,4]

        # [(24,96),(12,48),(-12,-3),(4,4)]

        # [2,4,-3,4]
        # [(-96,8), (-48,4),(-12,-3),(4,4)]

        # [1,2,-3,4]
        # [(0,0),(-24,2),(-12,-3),(4,4)]

        dp = [(float('inf'),float('-inf'))] * len(nums)

        dp[-1] = (nums[-1], nums[-1])
        
        for i in range(len(nums) -2, -1, -1):
            num = nums[i]

            minProduct = min(num * dp[i + 1][0], num * dp[i + 1][1], num)
            maxProduct = max(num * dp[i + 1][0], num * dp[i + 1][1], num)

            dp[i] = (minProduct, maxProduct)
        

        print(dp)
        return max([biggest for (small, biggest) in dp])




