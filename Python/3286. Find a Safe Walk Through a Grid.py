class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        max_health = [[-1] * n for _ in range(m)]
        
        initial_health = health - grid[0][0]
        if initial_health <= 0:
            return False
            
        queue = deque([(0, 0, initial_health)])
        max_health[0][0] = initial_health
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c, h = queue.popleft()
            
            if r == m - 1 and c == n - 1 and h >= 1:
                return True
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    cost = grid[nr][nc]
                    next_h = h - cost
                    
                    if next_h > 0 and next_h > max_health[nr][nc]:
                        max_health[nr][nc] = next_h
                        queue.append((nr, nc, next_h))
                        
        return False