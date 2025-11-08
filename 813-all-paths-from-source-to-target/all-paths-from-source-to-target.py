class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        target = n - 1

        def dfs(node, path):
            if node == target:
                res.append(path[:])

            for nei in graph[node]:
                path.append(nei)
                dfs(nei, path)
                path.pop()
                    
        dfs(0, [0])
        return res
