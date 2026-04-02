class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG_INF = float('-inf')

        dp = [[[NEG_INF]*3 for _ in range(n)] for _ in range(m)]

        for k in range(3):
            if coins[0][0] < 0 and k > 0:
                dp[0][0][k] = 0
            else:
                dp[0][0][k] = coins[0][0]

        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if i == 0 and j == 0:
                        continue

                    val = coins[i][j]

                    best = NEG_INF

                    if i > 0:
                        best = max(best, dp[i-1][j][k])
                    if j > 0:
                        best = max(best, dp[i][j-1][k])

                    if best != NEG_INF:
                        dp[i][j][k] = max(dp[i][j][k], best + val)

                    if val < 0 and k > 0:
                        best2 = NEG_INF
                        if i > 0:
                            best2 = max(best2, dp[i-1][j][k-1])
                        if j > 0:
                            best2 = max(best2, dp[i][j-1][k-1])

                        if best2 != NEG_INF:
                            dp[i][j][k] = max(dp[i][j][k], best2)

        return max(dp[m-1][n-1])