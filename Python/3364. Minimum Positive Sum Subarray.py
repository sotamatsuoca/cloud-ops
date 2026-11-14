class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        best = float('inf')
        for i in range(n):
            total = 0
            for j in range(i, min(n, i + r)):
                total += nums[j]
                if j - i + 1 >= l and total > 0:
                    best = min(best, total)
        return best if best != float('inf') else -1