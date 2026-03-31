class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        # What we need to do? Since we want to partition the array into two
        # subarrays that have the same sum, it means that we want to fing a 
        # subarray that sums up to half of the entire sum, if that sum doesn't
        # exits then we need to return false.


        # How should we do it? We're gonna set the target as half of the entire
        # sum and use a two pointer approach to get to the subarray that we want
        #
        # e.g: [1,2,3,4] target = (4 + 3 + 2 + 1 ) / 2 = 5
        # 
        # e.g II: [1,2,3,4,6,8] target = 12
        #                         []
        #                    [1,0]   [0,1]
        #                [3,0] [1,2] [2,1] [0,3]
        #            [6,0] [3,3] [4,2], [1,5]
        #          [10,0][6,4]
        #      [16,0][10,6][12,4][6,10]

        #    1,2,3,4,6,8
        # 1 [0,0,0,0,0,0]
        # 2 [0,0,0,0,0,0]
        # 3 [0,0,0,0,0,0]
        # 4 [0,0,0,0,0,0]
        # 6 [0,0,0,0,0,0]
        # 8 [0,0,0,0,0,0]

        #    0,1,2,3,4,5,6,7,8,9,10,11,12
        # 1 [0,0,0,0,0,0,0,0,0,0, 0, 0, 0]
        # 2 [0,0,0,0,0,0,0,0,0,0, 0, 0, 0]
        # 3 [0,0,0,0,0,0,0,0,0,0, 0, 0, 0]
        # 4 [0,0,0,0,0,0,0,0,0,0, 0, 0, 0]
        # 6 [0,0,0,0,0,0,0,0,0,0, 0, 0, 0]
        # 8 [8,0,0,0,1,0,0,0,0,0, 0, 0, 0] 
        #   [8,0,0,0,0,0,0,0,0,0, 0, 0, 0] 





        # What structure or algorithm should we use? We could use a DFS

        # What's the time complexity of this approach? O(2^n) which is not
        # really great


        nums.sort()

        target = sum(nums) / 2


        def dfs(i, leftSum, rightSum):

            if i == len(nums):
                return leftSum == target or rightSum == target
            

            if leftSum == target or rightSum == target:
                return True
            

            return (dfs(i + 1, leftSum + nums[i], rightSum) or
                dfs(i + 1, leftSum, rightSum + nums[i]))
            
        return dfs(0,0,0)









        







