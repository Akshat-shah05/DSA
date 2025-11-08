class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, weight in times:
            adjList[u].append((v, weight))
        
        pq = [(0, k)] # Time and node
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        while pq:
            time, node = heapq.heappop(pq)
            if time > dist[node]:
                continue
            
            dist[node] = time
            for nei, t in adjList[node]:
                newTime = time + t
                if newTime < dist[nei]:
                    heapq.heappush(pq, (newTime, nei))
        
        ans = max(dist[1:])
        return ans if ans != float('inf') else -1