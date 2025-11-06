class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjList = defaultdict(set)
        indegree = Counter({c: 0 for word in words for c in word})

        for first, second in zip(words, words[1:]):
            for c, d in zip(first, second):
                if c != d:
                    if d not in adjList[c]:
                        adjList[c].add(d)
                        indegree[d] += 1
                    break
            
            else:
                if len(second) < len(first):
                    return ""
        output = []
        q = deque([c for c in indegree if indegree[c] == 0])
        while q:
            c = q.popleft()
            output.append(c)
            for d in adjList[c]:
                indegree[d] -= 1
                if indegree[d] == 0:
                    q.append(d)
        
        if len(output) < len(indegree):
            return ""
        
        return "".join(output)