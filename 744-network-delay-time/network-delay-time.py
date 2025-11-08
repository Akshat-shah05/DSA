class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, weight in times:
            adj[u].append([v, weight])
        
        minHeap = [[0, k]]
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)
            if time > dist[node]:
                continue
            
            dist[node] = time
            for nei, time2 in adj[node]:
                newTime = time + time2
                if newTime < dist[nei]:
                    heapq.heappush(minHeap, [time2 + time, nei])
        
        ans = max(dist[1:])
        return -1 if ans == float('inf') else ans