class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adjList = defaultdict(list)
        parentList = defaultdict(int)
        indegrees = [0] * (n + 1)
        for prereq, postreq in relations:
            prereqTime = parentList[prereq] if prereq in parentList else time[prereq - 1]
            adjList[prereq].append(postreq)
            parentList[postreq] = max(parentList[postreq], prereqTime)
            indegrees[postreq] += 1
        
        maxTime = 0
        q = deque([(x, time[x - 1]) for x in range(1, n + 1) if indegrees[x] == 0])

        while q:
            course, t = q.popleft()
            maxTime = max(maxTime, t)

            for nei in adjList[course]:
                parentList[nei] = max(parentList[nei], t)
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append((nei, time[nei - 1] + parentList[nei]))

        return maxTime
        

        return maxTime