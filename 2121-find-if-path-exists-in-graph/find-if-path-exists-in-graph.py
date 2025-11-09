class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        seen = set()
        
        def dfs(src, dst):
            if src == dst:
                return True
            
            seen.add(src)
            for nei in adjList[src]:
                if nei not in seen:
                    if dfs(nei, dst):
                        return True
            
            return False
        
        return dfs(source, destination)