class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        dp = [INF] * (n + 1)
        ans = INF
        left = 0
        s = 0
        for right in range(n):
            s += arr[right]
            while s > target:
                s -= arr[left]
                left += 1
            dp[right + 1] = dp[right]
            if s == target:
                length = right - left + 1
                if dp[left] != INF:
                    ans = min(ans, dp[left] + length)
                dp[right + 1] = min(dp[right], length)
        return ans if ans != INF else -1