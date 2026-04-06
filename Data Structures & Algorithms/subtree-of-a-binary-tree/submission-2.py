# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:

    def createNodeArray(self, node):

        res = []
        q = deque([node])

        while q:
            cur_node = q.popleft()

            if cur_node:
                res.append(str(cur_node.val))
                q.append(cur_node.left)
                q.append(cur_node.right)
            else:
                res.append("None")
        print(res)
        return res


    def compareTrees(self, root, subroot):
        rootArray = self.createNodeArray(root)
        subArray = self.createNodeArray(subroot)
        print(rootArray)
        print(subArray)

        rootStr =  "|".join(rootArray)
        subStr = "|".join(subArray)

        if len(subStr) > len(rootStr): return False

        init, end = 0, len(subStr) - 1

        while end < len(rootStr):
            if rootStr[init: end + 1] == subStr:
                return True
            
            init += 1
            end += 1
        
        return False


        # return rootArray == subArray


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False

        isValid = False
        if root.val == subRoot.val:
            return self.compareTrees(root, subRoot)
        
        hasSubtreeL = self.isSubtree(root.left, subRoot)
        hasSubtreeR = self.isSubtree(root.right, subRoot)

        return isValid or hasSubtreeL or hasSubtreeR






