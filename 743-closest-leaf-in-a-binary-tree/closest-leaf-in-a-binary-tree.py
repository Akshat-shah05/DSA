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

        def dfs(root, parent=None):
            nonlocal start
            if root:
                if parent:
                    graph[root].append(parent)
                    graph[parent].append(root)
                
                if root.val == k:
                    start = root
                
                dfs(root.left, root)
                dfs(root.right, root)
        
        dfs(root)

        q = deque([start])
        visited = set([start])

        while q:
            node = q.popleft()
            if node:
                if not node.right and not node.left:
                    return node.val
            
                for nei in graph[node]:
                    if nei not in visited:
                        if not nei.right and not nei.left:
                            return nei.val
                        visited.add(nei)
                        q.append(nei)
            
