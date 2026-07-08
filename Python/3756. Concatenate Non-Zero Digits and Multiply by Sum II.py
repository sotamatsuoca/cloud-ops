class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        m = len(s)

        prefix_val = [0] * (m + 1)
        prefix_cnt = [0] * (m + 1)
        prefix_sum = [0] * (m + 1)
        pow10 = [1] * (m + 1)

        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        for i in range(m):
            d = int(s[i])
            if d != 0:
                prefix_val[i + 1] = (prefix_val[i] * 10 + d) % MOD
                prefix_cnt[i + 1] = prefix_cnt[i] + 1
                prefix_sum[i + 1] = prefix_sum[i] + d
            else:
                prefix_val[i + 1] = prefix_val[i]
                prefix_cnt[i + 1] = prefix_cnt[i]
                prefix_sum[i + 1] = prefix_sum[i]

        answer = []
        for l, r in queries:
            k = prefix_cnt[r + 1] - prefix_cnt[l]
            x = (prefix_val[r + 1] - prefix_val[l] * pow10[k]) % MOD
            total_sum = (prefix_sum[r + 1] - prefix_sum[l]) % MOD
            answer.append((x * total_sum) % MOD)

        return answer