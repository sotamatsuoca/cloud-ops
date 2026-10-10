class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        k = k1 + k2
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]

        if sum(diffs) <= k:
            return 0

        count = [0] * (max(diffs) + 1)
        for d in diffs:
            count[d] += 1

        cur = len(count) - 1
        while cur > 0 and k > 0:
            if count[cur] == 0:
                cur -= 1
                continue
            if count[cur] <= k:
                k -= count[cur]
                count[cur - 1] += count[cur]
                count[cur] = 0
                cur -= 1
            else:
                count[cur] -= k
                count[cur - 1] += k
                k = 0

        result = 0
        for value in range(len(count)):
            result += count[value] * value * value
        return result