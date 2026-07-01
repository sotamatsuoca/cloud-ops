class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
        
        thief_dist = [[float('inf')] * n for _ in range(n)]
        q = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    thief_dist[r][c] = 0
                    q.append((r, c))
                    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and thief_dist[nr][nc] == float('inf'):
                    thief_dist[nr][nc] = thief_dist[r][c] + 1
                    q.append((nr, nc))
                    
        max_heap = [(-thief_dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while max_heap:
            sf, r, c = heapq.heappop(max_heap)
            sf = -sf
            
            if r == n - 1 and c == n - 1:
                return sf
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    next_sf = min(sf, thief_dist[nr][nc])
                    heapq.heappush(max_heap, (-next_sf, nr, nc))
                    
        return 0