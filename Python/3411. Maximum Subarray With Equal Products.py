class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0
        for i in range(n):
            p = 1
            g = 0
            l = 1
            for j in range(i, n):
                x = nums[j]
                p *= x
                g = gcd(g, x)
                l = l * x // gcd(l, x)
                if p == l * g:
                    best = max(best, j - i + 1)
        return best