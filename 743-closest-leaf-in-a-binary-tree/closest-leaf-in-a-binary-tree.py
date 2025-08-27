# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        graph = defaultdict(list)
        start = None
        def dfs(node, parent = None):
            nonlocal start
            if not node:
                return 
            
            if node.val == k:
                start = node

            if parent is not None:
                graph[node].append(parent)
                graph[parent].append(node)
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root)
        q = deque([start]) 
        visited = set([start])
        while q:
            node = q.popleft()
            if not node.left and not node.right:
                return node.val
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        
