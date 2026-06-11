class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        MOD = 10**9 + 7
        
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        max_depth = 0
        queue = deque([(1, 0)])
        visited = {1}
        
        while queue:
            node, depth = queue.popleft()
            if depth > max_depth:
                max_depth = depth
                
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
                    
        return pow(2, max_depth - 1, MOD)