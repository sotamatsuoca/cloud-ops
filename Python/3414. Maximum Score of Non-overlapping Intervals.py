class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = sorted(range(n), key=lambda i: intervals[i][1])
        rs = [intervals[i][1] for i in arr]

        def find(l):
            lo, hi = 0, len(rs)
            while lo < hi:
                mid = (lo + hi) // 2
                if rs[mid] < l:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        for i in range(1, n + 1):
            orig = arr[i - 1]
            l, r, w = intervals[orig]
            p = find(l)
            dp[i][0] = (0, ())
            for k in range(1, 5):
                best = dp[i - 1][k]
                prevScore, prevIdx = dp[p][k - 1]
                candScore = prevScore + w
                candIdx = tuple(sorted(prevIdx + (orig,)))
                if candScore > best[0] or (candScore == best[0] and candIdx < best[1]):
                    best = (candScore, candIdx)
                dp[i][k] = best

        return list(dp[n][4][1])