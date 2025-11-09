class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []

        def dfs(src, path):
            nonlocal paths
            if src == n - 1:
                paths.append(path[:])
                return
            
            for nei in graph[src]:
                dfs(nei, path + [nei])

        dfs(0, [0])
        return paths