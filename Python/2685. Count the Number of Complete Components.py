class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1

        for a, b in edges:
            union(a, b)

        node_count = [0] * n
        edge_count = [0] * n

        for i in range(n):
            root = find(i)
            node_count[root] += 1

        for a, b in edges:
            root = find(a)
            edge_count[root] += 1

        result = 0
        for i in range(n):
            if find(i) == i:
                k = node_count[i]
                if edge_count[i] == k * (k - 1) // 2:
                    result += 1

        return result