class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f = sum(i * v for i, v in enumerate(nums))
        total_sum = sum(nums)
        n = len(nums)
        
        ans = f
        
        for k in range(1, n):
            f = f + total_sum - n * nums[n - k]
            ans = max(ans, f)
            
        return ans