# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        pts = []
        pte = []

        def path(root, target):
            path = []
            def dfs(root):
                if not root:
                    return False
                
                if root.val == target:
                    return True
                
                path.append("L")
                if dfs(root.left):
                    return True
                
                path.pop()
                path.append("R")
                if dfs(root.right):
                    return True
                
                path.pop()
                return False
            
            return ''.join(path) if dfs(root) else ''
        
        pts = path(root, startValue)
        pte = path(root, destValue)
        i = 0
        while i < len(pts) and i < len(pte) and pte[i] == pts[i]:
            i += 1
        
        return ("U" * (len(pts) - i)) + pte[i:]