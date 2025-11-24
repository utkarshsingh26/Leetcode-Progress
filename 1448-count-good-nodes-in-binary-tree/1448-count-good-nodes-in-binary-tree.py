# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = [0]

        def dfs(node, maximum):
            if not node:
                return
            
            if node.val >= maximum:
                count[0] += 1
                maximum = node.val
            
            if node.left:
                dfs(node.left, maximum)
            
            if node.right:
                dfs(node.right, maximum)
        
        dfs(root, float("-inf"))
        return count[0]