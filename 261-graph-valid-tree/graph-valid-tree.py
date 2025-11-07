class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        seen = set()
        visited = 0
        def dfs(start):
            nonlocal visited
            if start in seen:
                return
            
            seen.add(start)
            visited += 1
            for nei in adjList[start]:
                dfs(nei)
        
        dfs(0)
        return (len(edges) == n - 1) and visited == n