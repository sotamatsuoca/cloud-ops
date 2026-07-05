class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        dp = [[-1] * n for _ in range(n)]
        cnt = [[0] * n for _ in range(n)]
        dp[n-1][n-1] = 0
        cnt[n-1][n-1] = 1

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == n-1 and j == n-1:
                    continue
                if board[i][j] == 'X':
                    continue

                best = -1
                ways = 0
                for di, dj in ((1, 0), (0, 1), (1, 1)):
                    ni, nj = i + di, j + dj
                    if ni < n and nj < n and dp[ni][nj] >= 0:
                        if dp[ni][nj] > best:
                            best = dp[ni][nj]
                            ways = cnt[ni][nj]
                        elif dp[ni][nj] == best:
                            ways = (ways + cnt[ni][nj]) % MOD

                if best >= 0:
                    val = 0 if board[i][j] in ('E', 'S') else int(board[i][j])
                    dp[i][j] = best + val
                    cnt[i][j] = ways

        if dp[0][0] < 0:
            return [0, 0]
        return [dp[0][0], cnt[0][0] % MOD]