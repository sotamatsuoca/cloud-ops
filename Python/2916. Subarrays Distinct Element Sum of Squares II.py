class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        b1 = [0] * (n + 2)
        b2 = [0] * (n + 2)
        size = n + 1

        def upd(tree, i, v):
            while i <= size:
                tree[i] += v
                i += i & -i

        def qry(tree, i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & -i
            return s

        def prefix(i):
            return qry(b1, i) * i - qry(b2, i)

        last = {}
        s2 = 0
        ans = 0
        for r in range(n):
            p = last.get(nums[r], -1)
            lo = p + 2
            hi = r + 1
            length = hi - lo + 1
            range_sum = prefix(hi) - prefix(lo - 1)
            s2 += 2 * range_sum + length
            upd(b1, lo, 1)
            upd(b1, hi + 1, -1)
            upd(b2, lo, lo - 1)
            upd(b2, hi + 1, -hi)
            last[nums[r]] = r
            ans = (ans + s2) % MOD
        return ans