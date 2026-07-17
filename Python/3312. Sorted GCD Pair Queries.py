class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        from bisect import bisect_right

        m = max(nums)
        freq = [0] * (m + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (m + 1)
        for d in range(1, m + 1):
            s = 0
            for k in range(d, m + 1, d):
                s += freq[k]
            cnt[d] = s

        exact = [0] * (m + 1)
        for d in range(m, 0, -1):
            c = cnt[d]
            pairs = c * (c - 1) // 2
            for k in range(d * 2, m + 1, d):
                pairs -= exact[k]
            exact[d] = pairs

        vals = []
        pref = []
        cur = 0
        for d in range(1, m + 1):
            if exact[d]:
                vals.append(d)
                cur += exact[d]
                pref.append(cur)

        return [vals[bisect_right(pref, q)] for q in queries]