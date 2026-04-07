class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs(index, num_list, amount):

            if index >= len(nums):
                return

            if amount == target:
                nonlocal res
                print(amount, num_list)
                res.append(num_list.copy())
                return
            elif amount > target:
                return
            
            num_list.append(nums[index])
            dfs(index, num_list, amount + nums[index])

            num_list.pop()
            dfs(index + 1, num_list, amount)

        dfs(0, [], 0)
        return res