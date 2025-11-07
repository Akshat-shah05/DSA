class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(int)
        for u, v in edges:
            graph[u] += 1
            graph[v] += 1
        
        n = len(graph) - 1
        
        for i, v in graph.items():
            if v == n:
                return i
        