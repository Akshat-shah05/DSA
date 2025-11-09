class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # For any DAG, theres at least one node of indegree 0
        # Time for course = base time for course + max(time for parents)

        adjList = defaultdict(list)
        parentList = defaultdict(int)
        indegrees = [0] * (n + 1)
        for u, v in relations:
            adjList[u].append(v)
            indegrees[v] += 1
        
        q = deque([(i, time[i - 1]) for i in range(1, n + 1) if indegrees[i] == 0])

        timeTaken = 0

        while q:
            course, timeSoFar = q.popleft()
            timeTaken = max(timeTaken, timeSoFar)

            for nei in adjList[course]:
                parentList[nei] = max(parentList[nei], timeSoFar)
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append((nei, time[nei - 1] + parentList[nei]))
        
        return timeTaken

