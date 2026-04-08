# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # return dfs(node.val)
        res = None
        def dfs(node):


            if not node:
                return False

            if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
                nonlocal res
                res = node
                return
            
            if node.val < p.val:
                dfs(node.right)
            else:
                dfs(node.left)

        dfs(root)
        return res
