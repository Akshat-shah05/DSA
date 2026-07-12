class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v in roads:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        outdegrees = []
        for key, val in adj_list.items():
            outdegrees.append((key, len(val)))
        
        for i in range(n):
            if i not in adj_list:
                outdegrees.append((i, 0))
        
        sorted_outdegrees = sorted(outdegrees, key=lambda x : x[1])
        idx_to_importance = defaultdict(int)
        for i in range(n, 0, -1):
            idx_to_importance[sorted_outdegrees[i - 1][0]] = i
        
        importance = 0

        for u, v in roads:
            importance += idx_to_importance[u] + idx_to_importance[v]
        
        return importance