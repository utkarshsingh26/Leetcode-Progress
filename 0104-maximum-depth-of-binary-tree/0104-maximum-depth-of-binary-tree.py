# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)

            depth = 1 + max(left, right)

            return depth
        
        return height(root)
