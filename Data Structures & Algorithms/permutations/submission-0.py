class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def dfs(visited, index, permutation):
            print(visited, index, permutation)
            if len(permutation) == len(nums):
                print(visited, index, permutation)
                res.append(permutation.copy())

            visited.add(index)
            
            for i, num in enumerate(nums):

                if i not in visited:
                    permutation.append(num)
                    dfs(visited, i, permutation)
                    permutation.pop()
            
            visited.remove(index)
        
        for i, num in enumerate(nums):
            dfs(set(), i, [num])
        return res
            
            