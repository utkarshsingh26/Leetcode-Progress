# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good = [0]

        def dfs(node, max_val):
            if not node:
                return None
            
            if node.val >= max_val:
                good[0] += 1
                max_val = node.val
            
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        
        dfs(root, root.val)
        return good[0]