# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        is_balanced = [True]

        def dfs(left, node, right):
            if not(left < node.val < right):
                is_balanced[0] = False
            
            if node.left:
                dfs(left, node.left, node.val)
            
            if node.right:
                dfs(node.val, node.right, right)
        
        dfs(float("-inf"), root, float('inf'))
        return is_balanced[0]