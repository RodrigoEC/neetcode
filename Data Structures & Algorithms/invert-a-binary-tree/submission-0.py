# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        # What we need to do?
        # For each node we need to invert their children, which
        # means that the left child is going to become the right
        # one and the right one the left.
        # 

        # How should we do it?
        #
        # We're going to make a sort of depth approach where for
        # each node we're going to invert it's children
        #
        #.          1
        #      2        5
        #  5.    2.        4
        #  

        # What's the time and space complexity?
        # - Time: O(2^n) -> n = numer of layer or O(number of nodes)
        # - Space: O(1)
        def invertNode(node):
            if not node:
                return

            invertNode(node.left)
            invertNode(node.right)
            
            node.left, node.right = node.right, node.left


        invertNode(root)
        return root