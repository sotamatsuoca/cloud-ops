class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float("inf")

        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = INF
                for d in range(1, length):
                    if length % d != 0:
                        continue
                    changes = 0
                    for g in range(d):
                        a = i + g
                        b = i + g + (length // d - 1) * d
                        while a < b:
                            if s[a] != s[b]:
                                changes += 1
                            a += d
                            b -= d
                    if changes < best:
                        best = changes
                cost[i][j] = best

        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for j in range(1, n + 1):
            for t in range(1, k + 1):
                for i in range(0, j - 1):
                    if dp[i][t - 1] == INF or cost[i][j - 1] == INF:
                        continue
                    val = dp[i][t - 1] + cost[i][j - 1]
                    if val < dp[j][t]:
                        dp[j][t] = val

        return dp[n][k]