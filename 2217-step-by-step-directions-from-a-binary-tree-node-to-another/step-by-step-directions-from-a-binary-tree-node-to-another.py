# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = defaultdict(list)
        start = None

        def dfs(root, parent=None):
            nonlocal start
            if root:
                if parent:
                    graph[root].append(parent)
                    graph[parent].append(root)
                
                if root.val == startValue:
                    start = root
                
                dfs(root.left, root)
                dfs(root.right, root)
            
        dfs(root)

        q = deque([(start, "")])
        visited = set([start])

        while q:
            node, path = q.popleft()

            if node.val == destValue:
                return path
            
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    if nei == node.left:
                        q.append((nei, path + "L"))
                    
                    elif nei == node.right:
                        q.append((nei, path + "R"))

                    else:
                        q.append((nei, path + "U"))
        
        return ""