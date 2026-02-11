# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        is_valid = [True]

        def dfs(minimum, node, maximum):
            if not node:
                return True
            
            if not(minimum < node.val < maximum):
                is_valid[0] = False
            
            return dfs(minimum, node.left, node.val) and dfs(node.val, node.right, maximum)
        
        dfs(float("-inf"), root, float("inf"))
        return is_valid[0]