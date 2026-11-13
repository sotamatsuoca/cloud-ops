class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        st = []
        bot = 0
        total = 0
        r = n - 1
        ans = 0

        for l in range(n - 1, -1, -1):
            v = nums[l]
            cnt = 1
            while len(st) > bot and st[-1][0] <= v:
                seg = st.pop()
                total -= seg[0] * seg[1]
                cnt += seg[1]
            st.append([v, cnt])
            total += v * cnt

            while total - (pre[r + 1] - pre[l]) > k:
                total -= st[bot][0]
                st[bot][1] -= 1
                if st[bot][1] == 0:
                    bot += 1
                r -= 1

            ans += r - l + 1

        return ans