# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        # What we need to do?
        # We need to calculate the size of biggest path in between two
        # nodes that exists in a given binary tree.
        #
        # How should we do it?
        # 
        # longest_path = 3
        #
        #           0 -> 
        #           1
        #       2       4
        #   3              8
        #
        #
        #
        #

        # longest_path = 0
        #
        #
         
        global longest_path 
        longest_path = 0

        def find_diameter(node, parent_path_size):

            if not node:
                return 0

            left_path = find_diameter(node.left, parent_path_size + 1)
            right_path = find_diameter(node.right, parent_path_size + 1)

            if (left_path + right_path - 1 >= parent_path_size + left_path or
                left_path + right_path - 1 >= parent_path_size + right_path):
                global longest_path 
                longest_path = max(left_path + right_path, longest_path)
            
            return max(left_path, right_path) + 1


        find_diameter(root, 0)
        return longest_path



