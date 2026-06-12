class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        LOG = 18
        up = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)
        
        q = [1]
        head = 0
        while head < len(q):
            u = q[head]
            head += 1
            for v in adj[u]:
                if v != up[0][u] and v != 1:
                    if up[0][v] == 0:
                        up[0][v] = u
                        depth[v] = depth[u] + 1
                        q.append(v)
                        
        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[j][i] = up[j-1][up[j-1][i]]
                
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[j][u]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]
            return up[0][u]

        MOD = 10**9 + 7
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
            lca = get_lca(u, v)
            d = depth[u] + depth[v] - 2 * depth[lca]
            ans.append(pow2[d - 1])
        return ans