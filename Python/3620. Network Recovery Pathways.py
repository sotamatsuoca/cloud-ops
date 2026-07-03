class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        n = len(online)
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        max_edge_cost = 0

        for u, v, cost in edges:
            graph[u].append((v, cost))
            in_degree[v] += 1
            if cost > max_edge_cost:
                max_edge_cost = cost

        queue = [i for i in range(n) if in_degree[i] == 0]
        topo_order = []
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            topo_order.append(u)
            for v, _ in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        def can_reach(min_allowed_cost: int) -> bool:
            dp = [float('inf')] * n
            dp[0] = 0

            for u in topo_order:
                current_cost = dp[u]
                if current_cost == float('inf'):
                    continue

                for v, cost in graph[u]:
                    if online[v] and cost >= min_allowed_cost:
                        next_cost = current_cost + cost
                        if next_cost < dp[v]:
                            dp[v] = next_cost

            return dp[n - 1] <= k

        low = 0
        high = max_edge_cost
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if can_reach(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans