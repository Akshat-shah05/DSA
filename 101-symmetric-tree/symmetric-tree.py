# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right

        def symmetric(l, r):
            if not l and r:
                return False
            
            if l and not r:
                return False
            
            if not l and not r:
                return True
            
            if l.val != r.val:
                return False
            
            return True and symmetric(l.left, r.right) and symmetric(l.right, r.left)
        
        return symmetric(left, right)
        