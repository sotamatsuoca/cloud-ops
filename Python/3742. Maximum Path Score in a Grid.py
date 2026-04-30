class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * (k + 1) for _ in range(n)]
        
        v0 = grid[0][0]
        c0 = 1 if v0 > 0 else 0
        if c0 <= k:
            dp[0][c0] = v0
            
        for i in range(m):
            new_dp = [[-1] * (k + 1) for _ in range(n)]
            for j in range(n):
                val = grid[i][j]
                cost = 1 if val > 0 else 0
                
                if i == 0 and j == 0:
                    new_dp[0] = dp[0]
                    continue
                
                for c in range(cost, k + 1):
                    res = -1
                    if i > 0 and dp[j][c - cost] != -1:
                        res = max(res, dp[j][c - cost] + val)
                    
                    if j > 0 and new_dp[j-1][c - cost] != -1:
                        res = max(res, new_dp[j-1][c - cost] + val)
                    
                    new_dp[j][c] = res
            dp = new_dp

        ans = max(dp[n-1])
        return ans if ans >= 0 else -1