class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)

        for i, v in enumerate(equations):
            A, B = v
            adjList[A].append((B, values[i]))
            adjList[B].append((A, 1/values[i]))
        
        def bfs(start, end):
            if start not in adjList or end not in adjList:
                return -1.0

            visited = set([(start)])
            q = deque([(start, 1)])
        
            while q:
                node, res = q.popleft()
                if node == end:
                    return res
                
                visited.add(node)
                for nei, weight in adjList[node]:
                    if nei in visited:
                        continue
                    
                    q.append((nei, res * weight))
            
            return -1.0
        
        ans = []

        for C, D in queries:
            ans.append(bfs(C, D))
        
        return ans