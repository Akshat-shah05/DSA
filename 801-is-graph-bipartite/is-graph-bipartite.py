class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for u in range(len(graph)):
            adj_list[u] = graph[u][:]

        seen = {}
        def check(adj_list, start, seen):
            q = deque([(start, 1)])
            while len(q) > 0:
                pop, color = q.popleft()
                if pop in seen:
                    if seen[pop] != color:
                        return False
                    continue
                
                seen[pop] = color
                vertices = graph[pop]
                for v in vertices:
                    q.append((v, -color))
            
            return True

        for i in range(len(graph)):
            if i not in seen:
                if check(adj_list, i, seen) == False:
                    return False
        
        return True

     