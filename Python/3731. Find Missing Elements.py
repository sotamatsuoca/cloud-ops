class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        lo, hi = min(nums), max(nums)
        return [n for n in range(lo, hi + 1) if n not in num_set]