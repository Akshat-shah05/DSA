class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, weight in times:
            adjList[u].append((v, weight))
        
        pq = [(0, k)] # Time and node
        visit = set()
        t = 0

        while pq:
            time, node = heapq.heappop(pq)
            if node in visit:
                continue

            t = max(t, time)
            
            visit.add(node)
            for nei, t2 in adjList[node]:
                if nei not in visit:
                    newTime = time + t2
                    heapq.heappush(pq, (newTime, nei))
        
        return t if len(visit) == n else -1