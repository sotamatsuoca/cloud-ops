class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        k = nums[0]
        best = -1

        asc = True
        for i in range(n):
            if nums[i] != (i + k) % n:
                asc = False
                break
        if asc:
            r = (n - k) % n
            cost = r
            if k > 0:
                cost = min(cost, k + 2)
            best = cost

        desc = True
        for i in range(n):
            if nums[i] != (k - i) % n:
                desc = False
                break
        if desc:
            kp = (k + 1) % n
            rp = (n - kp) % n
            cost = 1 + min(kp, rp)
            if best == -1 or cost < best:
                best = cost

        return best