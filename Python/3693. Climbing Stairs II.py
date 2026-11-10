class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        for j in range(1, n + 1):
            for k in range(1, 4):
                i = j - k
                if i < 0:
                    break
                cand = dp[i] + costs[j - 1] + k * k
                if cand < dp[j]:
                    dp[j] = cand
        return dp[n]