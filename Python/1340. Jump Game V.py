class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n
        
        sorted_indices = sorted(range(n), key=lambda i: arr[i])
        
        for i in sorted_indices:
            for step in range(1, d + 1):
                prev_idx = i - step
                if prev_idx < 0 or arr[prev_idx] >= arr[i]:
                    break
                dp[i] = max(dp[i], dp[prev_idx] + 1)
                
            for step in range(1, d + 1):
                next_idx = i + step
                if next_idx >= n or arr[next_idx] >= arr[i]:
                    break
                dp[i] = max(dp[i], dp[next_idx] + 1)
                
        return max(dp)