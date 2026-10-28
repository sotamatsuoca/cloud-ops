class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                if i == 0 and j == 0:
                    dp[i][j] = 1 << v
                    continue
                reach = 0
                if i > 0:
                    reach |= dp[i - 1][j]
                if j > 0:
                    reach |= dp[i][j - 1]
                cur = 0
                while reach:
                    low = reach & -reach
                    x = low.bit_length() - 1
                    cur |= 1 << (x ^ v)
                    reach ^= low
                dp[i][j] = cur
        final = dp[m - 1][n - 1]
        return (final & -final).bit_length() - 1