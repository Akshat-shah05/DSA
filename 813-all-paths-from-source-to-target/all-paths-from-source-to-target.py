class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        seen = set()
        def dfs(src, path):
            nonlocal paths
            if src == n - 1:
                paths.append(path[:])
                return
            
            seen.add(src)
            for nei in graph[src]:
                if nei not in seen:
                    dfs(nei, path + [nei])
            
            seen.remove(src)

        dfs(0, [0])
        return paths