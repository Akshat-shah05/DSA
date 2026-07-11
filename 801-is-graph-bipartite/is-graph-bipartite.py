class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n

        for start in range(n):
            if colors[start] != -1:
                continue

            colors[start] = 0
            q = deque([start])

            while q:
                node = q.popleft()

                for neighbor in graph[node]:
                    if colors[neighbor] == -1:
                        colors[neighbor] = 1 - colors[node]
                        q.append(neighbor)
                    
                    elif colors[neighbor] == colors[node]:
                        return False
            
        return True

     