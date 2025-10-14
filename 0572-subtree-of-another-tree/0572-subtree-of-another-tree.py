# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p,q):
            if not p and not q:
                return True
            elif (p and not q) or (q and not p) or (p.val != q.val):
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if (root and not subRoot) or (subRoot and not root):
            return False
        elif not root and not subRoot:
            return True
        elif root.val == subRoot.val:
            if isSameTree(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        elif root.val != subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        