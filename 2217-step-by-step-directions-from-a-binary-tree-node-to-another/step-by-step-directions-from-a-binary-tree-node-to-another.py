# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parentMap = {}
        graph = defaultdict(list)
        start = None

        def dfs(node, parent = None):
            nonlocal start
            if not node:
                return 
            if node.val == startValue:
                start = node
            
            if parent:
                parentMap[node] = parent
                graph[parent].append(node)
                graph[node].append(parent)
            
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root)
        
        q = deque([(start, "")])
        seen = set([start])
        while q:
            node, path = q.popleft()

            if node.val == destValue:
                return path

            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    if node in parentMap and parentMap[node] == nei:
                        q.append((nei, path + "U"))
 
                    elif node.left == nei:
                        q.append((nei, path + "L"))
                    
                    elif node.right == nei:
                        q.append((nei, path + "R"))
        