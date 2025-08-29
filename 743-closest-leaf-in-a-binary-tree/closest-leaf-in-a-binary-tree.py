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
            
            graph[node].append(parent)
            graph[parent].append(node)
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root)
        
        q2 = deque([start])
        seen = set()
        while q2:
            node = q2.popleft()
            if node:
                if not node.left and not node.right:
                    return node.val
                
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q2.append(nei)
                        
            for nei in graph[node]:
                if nei not in seen:
                    q2.append(nei)