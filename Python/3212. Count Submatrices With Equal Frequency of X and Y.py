class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        
        x = [[0] * (n + 1) for _ in range(m + 1)]
        y = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                x[i + 1][j + 1] = (grid[i][j] == 'X') + x[i][j + 1] + x[i + 1][j] - x[i][j]
                y[i + 1][j + 1] = (grid[i][j] == 'Y') + y[i][j + 1] + y[i + 1][j] - y[i][j]
                
                if x[i + 1][j + 1] > 0 and x[i + 1][j + 1] == y[i + 1][j + 1]:
                    ans += 1
                    
        return ans