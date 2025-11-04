class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        indegrees = [0] * numCourses
        for A, B in prerequisites:
            adjList[B].append(A)
            indegrees[A] += 1
        
        q = deque([x for x in range(numCourses) if indegrees[x] == 0])
        processed = 0

        while q:
            node = q.popleft()
            processed += 1

            for nei in adjList[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        
        return processed == numCourses

