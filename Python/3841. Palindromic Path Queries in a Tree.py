class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        size = [1] * n
        cur = [1 << (ord(ch) - 97) for ch in s]
        base = [0] * n

        order = []
        visited = [False] * n
        stack = [0]
        visited[0] = True
        base[0] = cur[0]
        while stack:
            v = stack.pop()
            tin[v] = len(order)
            order.append(v)
            for w in adj[v]:
                if not visited[w]:
                    visited[w] = True
                    up[0][w] = v
                    depth[w] = depth[v] + 1
                    base[w] = base[v] ^ cur[w]
                    stack.append(w)

        for i in range(n - 1, 0, -1):
            v = order[i]
            size[up[0][v]] += size[v]

        for k in range(1, LOG):
            prev = up[k - 1]
            row = up[k]
            for v in range(n):
                row[v] = prev[prev[v]]

        tree = [0] * (n + 2)

        def bit_update(i, x):
            i += 1
            while i <= n + 1:
                tree[i] ^= x
                i += i & -i

        def bit_query(i):
            i += 1
            r = 0
            while i > 0:
                r ^= tree[i]
                i -= i & -i
            return r

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            k = 0
            while diff:
                if diff & 1:
                    a = up[k][a]
                diff >>= 1
                k += 1
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return up[0][a]

        answer = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new = 1 << (ord(parts[2]) - 97)
                x = cur[u] ^ new
                if x:
                    bit_update(tin[u], x)
                    bit_update(tin[u] + size[u], x)
                    cur[u] = new
            else:
                u = int(parts[1])
                v = int(parts[2])
                l = lca(u, v)
                pu = base[u] ^ bit_query(tin[u])
                pv = base[v] ^ bit_query(tin[v])
                m = pu ^ pv ^ cur[l]
                answer.append(m & (m - 1) == 0)
        return answer