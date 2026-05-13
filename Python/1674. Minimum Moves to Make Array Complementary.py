class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            
            min_s = min(a, b) + 1
            max_s = max(a, b) + limit
            
            diff[2] += 2
            diff[min_s] -= 1
            diff[max_s + 1] += 1
            
            current_sum = a + b
            diff[current_sum] -= 1
            diff[current_sum + 1] += 1
            
        return min(list(accumulate(diff))[2 : 2 * limit + 1])