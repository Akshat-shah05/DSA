# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        pathToStart = []
        pathToEnd = []
        
        def path_finder(root, target):
            path = []
            def dfs(root, target):
                nonlocal path
                if not root:
                    return False
                if root.val == target:
                    return True
                
                path.append("L")
                if dfs(root.left, target):
                    return True
                
                path.pop()
                path.append("R")
                if dfs(root.right, target):
                    return True
                
                path.pop()
                return False
            
            return ''.join(path) if dfs(root, target) else None
                
        pathToStart = path_finder(root, startValue)
        pathToEnd = path_finder(root, destValue)
        
        i = 0
        while i < len(pathToStart) and i < len(pathToEnd) and pathToStart[i] == pathToEnd[i]:
            i += 1
        
        return ("U" * (len(pathToStart) - i)) + pathToEnd[i:]

                
        
