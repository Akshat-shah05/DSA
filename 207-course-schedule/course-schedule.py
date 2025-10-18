class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            adjList[b].append(a)
            indegrees[a] += 1
        
        q = deque([course for course in range(numCourses) if indegrees[course] == 0])
        processed_nodes = 0

        while q:
            curNode = q.popleft()
            processed_nodes += 1

            for node in adjList[curNode]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    q.append(node)
        
        return processed_nodes == numCourses
