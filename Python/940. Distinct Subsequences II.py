class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26
        total = 0
        for ch in s:
            idx = ord(ch) - ord('a')
            new_total = (2 * total + 1) % MOD
            new_total = (new_total - dp[idx]) % MOD
            dp[idx] = (total + 1) % MOD
            total = new_total
        return total % MOD