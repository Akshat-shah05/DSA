class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adjList = defaultdict(list)
        indegrees = [0] * (n + 1)
        for A, B in relations:
            adjList[A].append(B)
            indegrees[B] += 1
        
        q = deque([x for x in range(1, n + 1) if indegrees[x] == 0])
        sems = 0
        processed = 0

        while q:
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                processed += 1

                for nei in adjList[node]:
                    indegrees[nei] -= 1
                    if indegrees[nei] == 0:
                        q.append(nei)

            sems += 1
        
        return sems if processed == n else -1