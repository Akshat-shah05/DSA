class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        q = deque([[0]])
        target = n - 1
        res = []

        while q:
            path = q.popleft()
            mostRecentNode = path[-1]

            if mostRecentNode == target:
                res.append(path)
                continue
            
            for nei in graph[mostRecentNode]:
                q.append(path + [nei])
        
        return res

