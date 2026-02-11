# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []

        def bfs(node):
            if not node:
                return None
            
            queue = deque()
            queue.append(node)

            while queue:
                level_length = len(queue)
                level = []
                for _ in range(level_length):

                    treeNode = queue.popleft()

                    if treeNode.left:
                        queue.append(treeNode.left)
                    
                    if treeNode.right:
                        queue.append(treeNode.right)
        
                    level.append(treeNode.val)
                
                result.append(level)
        
        bfs(root)
        return result