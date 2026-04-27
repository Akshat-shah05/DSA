# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(root):
            nonlocal ans
            if not root:
                return 
            
            if root.left:
                dfs(root.left)
            
            ans.append(root.val)

            if root.right:
                dfs(root.right)
        
        dfs(root)
        return ans

       