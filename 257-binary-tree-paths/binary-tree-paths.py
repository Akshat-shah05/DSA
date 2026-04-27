# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(root, path):
            nonlocal paths
            if not root:
                return
            if not root.left and not root.right:
                path += str(root.val) if path == "" else f'->{root.val}'
                paths.append(path[:])
                return
            
            path += str(root.val) if path == "" else f'->{root.val}'
            
            dfs(root.left, path)
            dfs(root.right, path)
        
        dfs(root, "")

        return paths
            
