class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(p for _, p in items)
        dp = [0] * (budget + 1)
        for i in range(n):
            f_i, p_i = items[i]
            gain = 1
            for j in range(n):
                if j != i and items[j][0] % f_i == 0:
                    gain += 1
            for b in range(budget, p_i - 1, -1):
                v = dp[b - p_i] + gain
                if v > dp[b]:
                    dp[b] = v
        best = 0
        for b in range(budget + 1):
            total = dp[b] + (budget - b) // min_price
            if total > best:
                best = total
        return best