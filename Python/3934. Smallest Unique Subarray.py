class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mod = (1 << 61) - 1
        base = 911382323
        pre = [0] * (n + 1)
        pw = [1] * (n + 1)
        for i in range(n):
            pre[i + 1] = (pre[i] * base + nums[i]) % mod
            pw[i + 1] = (pw[i] * base) % mod

        def has_unique(length):
            cnt = {}
            p = pw[length]
            for i in range(n - length + 1):
                h = (pre[i + length] - pre[i] * p) % mod
                cnt[h] = cnt.get(h, 0) + 1
            for v in cnt.values():
                if v == 1:
                    return True
            return False

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo