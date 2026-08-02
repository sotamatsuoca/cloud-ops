class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [row[:] for row in [piles[:]]]
        dp = [piles[i] for i in range(n)]
        for length in range(2, n + 1):
            new_dp = [0] * (n - length + 1)
            for i in range(n - length + 1):
                j = i + length - 1
                new_dp[i] = max(piles[i] - dp[i + 1] if i + 1 <= j - 1 or i + 1 == j else piles[i] - dp[i], piles[j] - dp[i])
            dp = new_dp
        return dp[0] > 0