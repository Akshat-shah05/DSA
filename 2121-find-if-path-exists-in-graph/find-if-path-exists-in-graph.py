class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        if source == destination:
            return True
            
        if source not in adjList or destination not in adjList:
            return False
        
        seen = set()
        
        def dfs(source):
            if source == destination:
                return True
            
            seen.add(source)
            
            ans = False
            for nei in adjList[source]:
                if nei not in seen:
                    ans = ans or dfs(nei)
            
            return ans
        
        return dfs(source)