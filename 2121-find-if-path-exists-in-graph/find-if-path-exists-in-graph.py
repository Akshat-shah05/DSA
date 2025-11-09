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
            ans = False
            for nei in adjList[src]:
                if nei not in seen:
                    ans = ans or dfs(nei, dst)
            
            return ans
        
        return dfs(source, destination)