class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)
        for eq, val in zip(equations, values):
            a, b = eq
            adjList[a].append((b, val))
            adjList[b].append((a, 1/val))
        
        def bfs(start, end):
            if start not in adjList or end not in adjList:
                return -1
            q = deque([(start, 1)])
            seen = set([(start)])

            while q:
                node, resSoFar = q.popleft()

                if node == end:
                    return resSoFar
                
                for nei, mult in adjList[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, resSoFar * mult))
            
            return -1
        
        ans = []
        for c, d in queries:
            ans.append(bfs(c, d))

        return ans
