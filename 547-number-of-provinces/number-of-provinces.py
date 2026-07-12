class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()

        def dfs(i):
            if i in seen:
                return 
            
            seen.add(i)
            
            for v in range(n):
                if v not in seen and isConnected[i][v] == 1:
                    dfs(v)

        provinces = 0
        for i in range(n):
            if i not in seen:
                provinces += 1
                dfs(i)
    
        return provinces