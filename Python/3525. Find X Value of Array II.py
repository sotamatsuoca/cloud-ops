class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        sz = 1
        while sz < n:
            sz *= 2

        kk = k * k
        identity = [0] * kk
        for s in range(k):
            identity[s * k + s] = 1

        full = [0] * (2 * sz)
        mat = [None] * (2 * sz)

        one = 1 % k
        for i in range(sz + n, 2 * sz):
            full[i] = one
            mat[i] = identity

        def make_leaf(v):
            r = v % k
            m = [0] * kk
            for s in range(k):
                m[s * k + (s * r) % k] = 1
            return r, m

        def merge_pair(lf, lm, rf, rm):
            fp = (lf * rf) % k
            nm = [0] * kk
            for s in range(k):
                base = s * k
                rbase = ((s * lf) % k) * k
                for t in range(k):
                    nm[base + t] = lm[base + t] + rm[rbase + t]
            return fp, nm

        for i in range(n):
            full[sz + i], mat[sz + i] = make_leaf(nums[i])

        for i in range(sz - 1, 0, -1):
            full[i], mat[i] = merge_pair(full[2 * i], mat[2 * i], full[2 * i + 1], mat[2 * i + 1])

        def update(idx, val):
            pos = sz + idx
            full[pos], mat[pos] = make_leaf(val)
            pos >>= 1
            while pos >= 1:
                full[pos], mat[pos] = merge_pair(full[2 * pos], mat[2 * pos], full[2 * pos + 1], mat[2 * pos + 1])
                pos >>= 1

        def query(l, r):
            l += sz
            r += sz + 1
            left_parts = []
            right_parts = []
            while l < r:
                if l & 1:
                    left_parts.append(l)
                    l += 1
                if r & 1:
                    r -= 1
                    right_parts.append(r)
                l >>= 1
                r >>= 1
            parts = left_parts + right_parts[::-1]
            cf, cm = full[parts[0]], mat[parts[0]]
            for p in parts[1:]:
                cf, cm = merge_pair(cf, cm, full[p], mat[p])
            return cf, cm

        start_s = one
        result = []
        for idx, val, s0, x in queries:
            update(idx, val)
            fp, m = query(s0, n - 1)
            result.append(m[start_s * k + x])

        return result