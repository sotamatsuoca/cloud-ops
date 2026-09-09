class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        d = 1
        low = 1
        while low <= n:
            high = min(n, 10 ** d - 1)
            commas = (d - 1) // 3
            total += (high - low + 1) * commas
            low = 10 ** d
            d += 1
        return total