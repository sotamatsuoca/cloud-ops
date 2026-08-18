class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for x in sorted(set(nums), reverse=True):
            count = 0
            for i in range(n - k + 1):
                if x in nums[i:i + k]:
                    count += 1
                    if count > 1:
                        break
            if count == 1:
                return x
        return -1