# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, isLeft):
            nonlocal ans
            if not root:
                return 
                
            if not root.left and not root.right and isLeft:
                ans += root.val
                return 
            
            dfs(root.left, True)
            dfs(root.right, False)
        
        dfs(root, False)
        return ans