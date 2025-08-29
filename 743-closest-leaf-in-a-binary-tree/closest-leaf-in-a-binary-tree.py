# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        graph = defaultdict(list)
        q = deque([root])
        start = None

        while q:
            node = q.popleft()
            if node.val == k:
                start = node
            
            if node.left:
                graph[node.left].append(node)
                graph[node].append(node.left)
                q.append(node.left)
            
            if node.right:
                graph[node.right].append(node)
                graph[node].append(node.right)
                q.append(node.right)
        
        q2 = deque([start])
        seen = set()
        while q2:
            node = q2.popleft()
            if not node.left and not node.right:
                return node.val
            
            seen.add(node)
            
            for nei in graph[node]:
                if nei not in seen:
                    q2.append(nei)