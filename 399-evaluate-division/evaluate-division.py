class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)

        for eq, val in zip(equations, values):
            A, B = eq
            adjList[A].append((B, val))
            adjList[B].append((A, 1/val))
        
        def dfs(start, end, result, visited):
            if start not in adjList or end not in adjList:
                return -1.0

            if start == end:
                return result
            
            visited.add(start)

            for nei, val in adjList[start]:
                if nei in visited:
                    continue
                
                ans = dfs(nei, end, result * val, visited)
                if ans != -1.0:
                    return ans
            
            return -1.0

        ans = []
        for A, B in queries:
            ans.append(dfs(A, B, 1, set()))

        return ans