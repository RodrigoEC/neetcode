# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(left_lim, right_lim, node):

            if not node:
                return True

            print(node.val, left_lim, right_lim)
            if node.val <= left_lim or node.val >= right_lim:
                print("entered", node.val, left_lim, right_lim)
                return False

            

            return dfs(left_lim, node.val, node.left) and dfs(node.val, right_lim, node.right)    

        return dfs(float("-inf"), float("inf"), root)