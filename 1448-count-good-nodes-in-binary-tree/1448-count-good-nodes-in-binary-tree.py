# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good = [0]

        def dfs(node, value):
            if not node:
                return
            
            if node.val >= value:
                good[0] += 1
                value = node.val
            
            if node.left:
                dfs(node.left, value)
            
            if node.right:
                dfs(node.right, value)
        
        dfs(root, root.val)
        return good[0]