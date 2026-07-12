from collections import defaultdict, deque
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        graph = defaultdict(list)

        # Only include edges whose endpoint characters differ.
        for child in range(1, n):
            par = parent[child]

            if s[child] != s[par]:
                graph[par].append(child)
                graph[child].append(par)

        def bfs(start: int):
            q = deque([(start, 1)])
            seen = {start}

            farthest_node = start
            farthest_distance = 1
            component_nodes = []

            while q:
                node, distance = q.popleft()
                component_nodes.append(node)

                if distance > farthest_distance:
                    farthest_node = node
                    farthest_distance = distance

                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        q.append((neighbor, distance + 1))

            return farthest_node, farthest_distance, component_nodes

        visited_components = set()
        answer = 1

        for node in range(n):
            if node in visited_components:
                continue

            # Find one endpoint of this component's diameter.
            endpoint, _, component_nodes = bfs(node)
            visited_components.update(component_nodes)

            # Find the diameter starting from that endpoint.
            _, diameter, _ = bfs(endpoint)
            answer = max(answer, diameter)

        return answer