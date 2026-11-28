class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        cnt = [0] * (n + 1)
        for f, p in items:
            cnt[f] += 1
        multiples = [0] * (n + 1)
        for v in range(1, n + 1):
            total = 0
            for m in range(v, n + 1, v):
                total += cnt[m]
            multiples[v] = total
        pm = min(p for f, p in items)
        bonus = []
        for f, p in items:
            d = multiples[f] - 1
            if d > 0 and p < 2 * pm:
                bonus.append((p, d))
        bonus.sort()
        rem = budget
        result = 0
        for p, d in bonus:
            take = min(d, rem // p)
            if take == 0:
                break
            rem -= take * p
            result += 2 * take
            if take < d:
                break
        result += rem // pm
        return result