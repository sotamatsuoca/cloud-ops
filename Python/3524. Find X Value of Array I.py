class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k
        for num in nums:
            val = num % k
            new_dp = [0] * k
            for r in range(k):
                if dp[r]:
                    new_dp[(r * val) % k] += dp[r]
            new_dp[val] += 1
            for x in range(k):
                result[x] += new_dp[x]
            dp = new_dp
        return result