class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)
        rank = {v: i + 1 for i, v in enumerate(vals)}
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)
        top = 1 << (m.bit_length() - 1)

        def update(i, c, v):
            while i <= m:
                cnt[i] += c
                sm[i] += v
                i += i & -i

        def query(kth):
            pos = 0
            c = 0
            s = 0
            step = top
            while step:
                np = pos + step
                if np <= m and c + cnt[np] < kth:
                    pos = np
                    c += cnt[np]
                    s += sm[np]
                step >>= 1
            value = vals[pos]
            return value, s + (kth - c) * value

        cost = [0] * (n - x + 1)
        total = 0
        half = (x + 1) // 2
        for i in range(n):
            update(rank[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                update(rank[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                med, left = query(half)
                right = total - left
                cost[i - x + 1] = med * half - left + right - med * (x - half)

        INF = 10 ** 18
        prev = [0] * (n + 1)
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(x, n + 1):
                cand = prev[i - x] + cost[i - x]
                cur[i] = cur[i - 1] if cur[i - 1] < cand else cand
            prev = cur
        return prev[n]