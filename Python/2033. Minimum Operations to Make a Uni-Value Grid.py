class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [val for row in grid for val in row]
        
        remainder = nums[0] % x
        for val in nums:
            if val % x != remainder:
                return -1
        
        nums.sort()
        median = nums[len(nums) // 2]
        
        return sum(abs(val - median) // x for val in nums)