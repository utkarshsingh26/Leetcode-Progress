# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        root = TreeNode(val=preorder[0])

        root_pos = inorder.index(root.val)

        left_tree = inorder[:root_pos]
        right_tree = inorder[root_pos+1:]

        root.left = self.buildTree(preorder[1:root_pos+1], inorder[:root_pos])
        root.right = self.buildTree(preorder[1+root_pos:], inorder[root_pos+1:])

        return root