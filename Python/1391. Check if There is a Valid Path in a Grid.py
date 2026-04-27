class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        
        while queue:
            r, c = queue.popleft()
            if r == m - 1 and c == n - 1:
                return True
            
            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    for dnr, dnc in directions[grid[nr][nc]]:
                        if nr + dnr == r and nc + dnc == c:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
                            break
                            
        return False