class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        best = -1
        left = 0
        current = 0
        for right in range(len(nums)):
            current += nums[right]
            while current > target and left <= right:
                current -= nums[left]
                left += 1
            if current == target:
                best = max(best, right - left + 1)
        return len(nums) - best if best != -1 else -1