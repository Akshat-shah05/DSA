class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)

        for i, v in enumerate(equations):
            A, B = v
            adjList[A].append((B, values[i]))
            adjList[B].append((A, 1/values[i]))
        
        ans = []

        def dfs(start, end, result, visited):
            if start not in adjList or end not in adjList:
                return -1.0

            if start == end:
                return result
            
            visited.add(start)
            
            for nei, weight in adjList[start]:
                if nei in visited:
                    continue

                res = dfs(nei, end, result * weight, visited)
                if res != -1.0:
                    return res
            
            return -1.0



        for C, D in queries:
            ans.append(dfs(C, D, 1, set()))
        
        return ans