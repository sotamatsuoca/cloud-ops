class Solution:                
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        
        for l in range(layers):
            layer = []
            for j in range(l, n - l): layer.append(grid[l][j])
            for i in range(l + 1, m - l): layer.append(grid[i][n - l - 1])
            for j in range(n - l - 2, l - 1, -1): layer.append(grid[m - l - 1][j])
            for i in range(m - l - 2, l, -1): layer.append(grid[i][l])
            
            k_eff = k % len(layer)
            rotated = layer[k_eff:] + layer[:k_eff]
            
            idx = 0
            for j in range(l, n - l): grid[l][j] = rotated[idx]; idx += 1
            for i in range(l + 1, m - l): grid[i][n - l - 1] = rotated[idx]; idx += 1
            for j in range(n - l - 2, l - 1, -1): grid[m - l - 1][j] = rotated[idx]; idx += 1
            for i in range(m - l - 2, l, -1): grid[i][l] = rotated[idx]; idx += 1
            
        return grid