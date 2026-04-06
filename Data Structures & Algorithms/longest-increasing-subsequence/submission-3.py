class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        # What we need to do?
        # 
        # nums = [9,1,4,2,3,3,7]
        #
        # 1 -> 2 -> 3 -> 7
        #
        #
        #
        # sequences = [1,4,2,3,2,2,1]

        res = [1] * len(nums)

        for i in range(len(nums) -1, -1, -1):

            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = max(res[i], 1 + res[j])
        
        print(res)
        return max(res)






