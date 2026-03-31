class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        


        # What we need to do? We need to create all possible subsets of a 
        # given array without repeating any subset, this could happen because
        # now we can have duplicates on this given array.

        # How should we do it? The biggest obstacle we're facing is now the
        # repeating thing. This means that if we have for example:

        # e.g 01: [1,7,7,2]
        # if we don't take a good care here th subsets could endup being
        # [[],[1,7],[1,7], ...] right? Because we computed all the subarrays
        # with one with all the repeated values, which is not what we want.
        # We just want to compute it once, once we do that we can skip all the
        # repeated values.
        # What's does this mean? It means that, since this is a backtrack problem
        # each value we are faced with two options "include the number on the
        # subset" or "not include the number on the subset", right? but everytime
        # we include a number we want to skip all its repeated siblings, because
        # if we don't do it, we'll be calculating "including this or not" all over
        # again and this will result on repeated values on the response array 

        # What's the structure or algorithm we're using? We'll use backtracking

        # What's the time complexity of this solution? this would be still O(2^n)
        # even when we have repeated values

        # e.g 02: [1,2,1]
        # res = []
        # array = [1,1,2]
        # nums = [1,1,2]

        res = []
        nums.sort()

        def backtracking(i, array):
            if (i == len(nums)):
                res.append(array.copy())
                return
            
            array.append(nums[i])
            backtracking(i + 1, array)

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:

                i += 1
            
            array.pop()
            backtracking(i + 1, array)
        
        backtracking(0, [])
        return res











