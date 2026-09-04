class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suff_min = [0] * n
        curr_min = float('inf')
        for i in range(n - 1, -1, -1):
            if nums[i] < curr_min:
                curr_min = nums[i]
            suff_min[i] = curr_min
            
        curr_max = -float('inf')
        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]
            if curr_max - suff_min[i] <= k:
                return i
        return -1