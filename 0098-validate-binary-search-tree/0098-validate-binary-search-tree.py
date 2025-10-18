# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(minimum, node, maximum):
            if not node:
                return True
            
            if not (minimum < node.val < maximum):
                return False
            
            left = dfs(minimum, node.left, node.val)
            right = dfs(node.val, node.right, maximum)

            if left and right:
                return True
            else:
                return False
        
        return dfs(float('-inf'), root, float('inf'))
        