class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        prefix = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                prefix[j][i + 1] = prefix[j][i] + grid[i][j]

        dp = [[-1] * 2 for _ in range(n + 1)]
        
        for h in range(n + 1):
            dp[h][0] = 0
            dp[h][1] = 0

        for j in range(1, n):
            new_dp = [[-1] * 2 for _ in range(n + 1)]
            for h in range(n + 1):
                for prev_h in range(h + 1):
                    if dp[prev_h][0] != -1:
                        score = prefix[j - 1][h] - prefix[j - 1][prev_h]
                        new_dp[h][0] = max(new_dp[h][0], dp[prev_h][0] + score)
                
                for prev_h in range(h, n + 1):
                    score = prefix[j][prev_h] - prefix[j][h]
                    prev_best = max(dp[prev_h][0], dp[prev_h][1])
                    if prev_best != -1:
                        new_dp[h][1] = max(new_dp[h][1], prev_best + score)
                
                if h == 0:
                    for prev_h in range(n + 1):
                        new_dp[0][0] = max(new_dp[0][0], dp[prev_h][0], dp[prev_h][1])
            dp = new_dp

        return max(max(row) for row in dp)