class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        def expand(left: int, right: int) -> None:
            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1
                if length >= k:
                    if dp[left] + 1 > dp[right + 1]:
                        dp[right + 1] = dp[left] + 1
                    return
                left -= 1
                right += 1

        for i in range(n):
            if dp[i] > dp[i + 1]:
                dp[i + 1] = dp[i]
            expand(i, i)
            expand(i, i + 1)

        return dp[n]