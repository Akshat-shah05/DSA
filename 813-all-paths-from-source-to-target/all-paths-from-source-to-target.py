class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        target = n - 1
        seen = set()

        def dfs(node, path):
            if node == target:
                res.append(path[:])

            for nei in graph[node]:
                if nei in seen:
                    continue
                
                seen.add(nei)
                path.append(nei)
                dfs(nei, path)
                path.pop()
                seen.remove(nei)
        
        dfs(0, [0])
        return res
