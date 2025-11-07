class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        tested = set()
        nodes = set()
        for a, b in edges:
            nodes.add(a)
            nodes.add(b)
            adjList[a].append(b)
            adjList[b].append(a)
        
        def dfs(node):
            if node in tested:
                return 
            
            tested.add(node)
            for nei in adjList[node]:
                if nei not in tested:
                    dfs(nei)
        
        components = 0
        while len(nodes) > 0:
            dfs(nodes.pop())
            nodes -= tested
            components += 1
        
        return components + (n - len(tested))
