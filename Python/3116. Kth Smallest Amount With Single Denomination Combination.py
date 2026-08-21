class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        subsets = []
        for mask in range(1, 1 << n):
            l = 1
            for i in range(n):
                if mask & (1 << i):
                    g = gcd(l, coins[i])
                    l = l // g * coins[i]
                    if l > 2 * 10**15:
                        l = 2 * 10**15 + 1
                        break
            bits = bin(mask).count("1")
            sign = 1 if bits % 2 == 1 else -1
            subsets.append((l, sign))

        def count(x):
            total = 0
            for l, sign in subsets:
                if l <= x:
                    total += sign * (x // l)
            return total

        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo