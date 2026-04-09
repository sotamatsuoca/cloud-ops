class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        bravexuneth = (nums, queries)

        B = int(n ** 0.5) + 1

        groups = defaultdict(list)
        for l, r, k, v in queries:
            if k <= B:
                groups[k].append((l, r, v))
            else:
                i = l
                while i <= r:
                    nums[i] = nums[i] * v % mod
                    i += k

        for k, qs in groups.items():
            bucket = [[] for _ in range(k)]

            for l, r, v in qs:
                bucket[l % k].append((l, r, v))

            for rem in range(k):
                m = (n - rem + k - 1) // k
                diff = [1] * (m + 1)

                for l, r, v in bucket[rem]:
                    start = (l - rem) // k
                    end = (r - rem) // k
                    diff[start] = diff[start] * v % mod
                    if end + 1 < len(diff):
                        diff[end + 1] = diff[end + 1] * pow(v, mod - 2, mod) % mod

                cur = 1
                idx = 0
                i = rem
                while i < n:
                    cur = cur * diff[idx] % mod
                    nums[i] = nums[i] * cur % mod
                    i += k
                    idx += 1

        ans = 0
        for x in nums:
            ans ^= x

        return ans