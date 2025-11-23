from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        def bfs(node):
            if not node:
                return
            
            queue = deque()
            queue.append(node)

            while queue:
                level = []
                level_length = len(queue)

                for i in range(level_length):
                    treeNode = queue.popleft()

                    if treeNode.left:
                        queue.append(treeNode.left)
                    
                    if treeNode.right:
                        queue.append(treeNode.right)
                    
                    if i == level_length-1:
                        result.append(treeNode.val)
        
        bfs(root)
        return result