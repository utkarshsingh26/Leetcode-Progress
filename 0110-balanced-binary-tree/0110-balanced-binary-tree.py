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
            
            left = height(node.left)
            right = height(node.right)

            diff = abs(right - left)

            if diff > 1:
                is_balanced[0] = False

            return 1 + max(left, right)
        
        height(root)

        return is_balanced[0]