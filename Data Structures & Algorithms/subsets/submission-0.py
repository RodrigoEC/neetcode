class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        # What we need to do? Since we know that all integers are unique we
        # basically for each integer we can choose to include that integer
        # on the subset array or not

        # e.g 01 - [1,2,3]

        #                           []
        #                        [1]  []
        #                   [1,2]  [1][2] []
        #              [1,2,3][1,2][1,3][1][2,3][2][3][]

        # Because we want to return all possible values we will have to
        # find and run every possible option

        # How should we do it? We can run a DFS that receives an array and
        # the current position we're in the nums list when we get to the
        # last position we add a copy of the array to the response

        # What structure or algorithm can we use? A DFS algorithm

        # What's time complexity of this approach? O(2^n) and we can't optmize
        # this solution because we will have to run every possibility


        res = []

        def dfs(index, array):

            if (index == len(nums)):
                res.append(array.copy())
                return
            
            array.append(nums[index])
            dfs(index + 1, array)
            array.pop()
            dfs(index + 1, array)


        dfs(0, [])

        return res