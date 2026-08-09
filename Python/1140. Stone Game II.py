class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        memo = {}

        def dp(i, m):
            if i >= n:
                return 0
            if i + 2 * m >= n:
                return suffix_sum[i]
            if (i, m) in memo:
                return memo[(i, m)]

            best = 0
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                taken = suffix_sum[i] - dp(i + x, max(m, x))
                if taken > best:
                    best = taken

            memo[(i, m)] = best
            return best

        return dp(0, 1)