class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + (1 if i < n - 1 and nums[i] > nums[i + 1] else 0)
        nxt = [n] * (n + 1)
        for i in range(n - 1, -1, -1):
            if i < n - 1 and nums[i] > nums[i + 1]:
                nxt[i] = i
            else:
                nxt[i] = nxt[i + 1]
        total = 0
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            prev_max = 0
            ok = True
            for s in range(0, n, k):
                inner = pre[s + k - 1] - pre[s]
                if inner > 1:
                    ok = False
                    break
                if inner == 0:
                    lo = nums[s]
                    hi = nums[s + k - 1]
                else:
                    if nums[s + k - 1] > nums[s]:
                        ok = False
                        break
                    p = nxt[s]
                    lo = nums[p + 1]
                    hi = nums[p]
                if lo < prev_max:
                    ok = False
                    break
                prev_max = hi
            if ok:
                total += k
        return total