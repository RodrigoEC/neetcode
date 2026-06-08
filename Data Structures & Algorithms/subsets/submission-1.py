class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        # nums = [1,2,3]
        #
        #
        #
        # [] -> [1] -> [1]
        # [] -> [1] -> [1]
        # [] -> [1] -> [1,2]
        # [] -> [] -> [2]
        # [] -> [] -> []
        #
        #
        # []
        #.[3]
        #
        


        res = []
        def dfs(sublist: list, index: int):
            print(sublist)
            if index == len(nums):
                res.append(sublist.copy())
                return
            

            dfs(sublist, index + 1)
            sublist.append(nums[index])
            dfs(sublist, index + 1)

            sublist.pop()

        
        dfs([], 0)
        return res
            
            

