# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        is_balanced = [True]

        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)

            difference = abs(left_height - right_height)

            if difference > 1:
                is_balanced[0] = False

            return 1 + max(left_height, right_height)
        
        height(root)
        return is_balanced[0]
        