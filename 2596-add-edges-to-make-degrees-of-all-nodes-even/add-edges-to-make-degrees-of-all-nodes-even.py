class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        for i in range(1, n + 1):
            if i not in adj_list:
                adj_list[i] = []
        
        odd_degree_nodes = []

        for key, val in adj_list.items():
            if len(val) % 2 != 0:
                odd_degree_nodes.append(key)
        
        num_odd = len(odd_degree_nodes)
        if num_odd == 0:
            return True
        
        if num_odd not in (2, 4):
            return False

        if num_odd == 2:
            a, b = odd_degree_nodes

            # Add one edge directly between the odd nodes.
            if b not in adj_list[a]:
                return True

            # Add a-x and b-x for some third node x.
            for x in range(1, n + 1):
                if x != a and x != b:
                    if x not in adj_list[a] and x not in adj_list[b]:
                        return True

            return False

        a, b, c, d = odd_degree_nodes

        # Try all three ways to pair four nodes.
        return (
            (b not in adj_list[a] and d not in adj_list[c])
            or
            (c not in adj_list[a] and d not in adj_list[b])
            or
            (d not in adj_list[a] and c not in adj_list[b])
        )