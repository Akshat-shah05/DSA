# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        graph = defaultdict(list)
        q1 = deque([root])
        start = None
        while q1:
            node = q1.popleft()
            if node.val == k:
                start = node
            
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                q1.append(node.left)
            
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                q1.append(node.right)


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
        
