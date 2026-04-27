# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hmap = defaultdict(int)
        best = float('-inf')

        def dfs(root):
            nonlocal hmap
            nonlocal best
            if not root:
                return 
            
            hmap[root.val] += 1
            best = max(hmap[root.val], best)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        modes = []
        for key, val in hmap.items():
            if val == best:
                modes.append(key)
        
        return modes


        