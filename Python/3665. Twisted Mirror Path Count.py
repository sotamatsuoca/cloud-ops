class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        rr = [[-1] * (n + 1) for _ in range(m + 1)]
        rd = [[-1] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    rr[i][j] = i * n + j
                    rd[i][j] = i * n + j
                else:
                    rr[i][j] = rd[i + 1][j] if i + 1 < m else -1
                    rd[i][j] = rr[i][j + 1] if j + 1 < n else -1
        dp = [0] * (m * n)
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                cur = dp[i * n + j]
                if cur == 0:
                    continue
                if j + 1 < n:
                    t = rr[i][j + 1]
                    if t >= 0:
                        dp[t] = (dp[t] + cur) % MOD
                if i + 1 < m:
                    t = rd[i + 1][j]
                    if t >= 0:
                        dp[t] = (dp[t] + cur) % MOD
        return dp[m * n - 1] % MOD