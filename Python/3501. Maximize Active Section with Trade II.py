class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], i, j - 1))
            i = j
        m = len(runs)
        pos_to_run = [0] * n
        for idx, (c, st, en) in enumerate(runs):
            for p in range(st, en + 1):
                pos_to_run[p] = idx
        lengths = [en - st + 1 for (c, st, en) in runs]
        NEG = float('-inf')
        val = [NEG] * m
        for j in range(1, m - 1):
            if runs[j][0] == '1':
                val[j] = lengths[j - 1] + lengths[j + 1]
        log_table = [0] * (m + 1)
        for i in range(2, m + 1):
            log_table[i] = log_table[i // 2] + 1
        st_table = [val[:]]
        jbit = 1
        while (1 << jbit) <= m:
            prev = st_table[-1]
            half = 1 << (jbit - 1)
            length = m - (1 << jbit) + 1
            cur = [max(prev[i], prev[i + half]) for i in range(length)]
            st_table.append(cur)
            jbit += 1

        def query_max(l, r):
            if l > r:
                return NEG
            length = r - l + 1
            k = log_table[length]
            return max(st_table[k][l], st_table[k][r - (1 << k) + 1])

        totalOnes = s.count('1')
        ans = []
        for l, r in queries:
            a = pos_to_run[l]
            b = pos_to_run[r]
            if b - a <= 1:
                gain = 0
            else:
                lo, hi = a + 1, b - 1
                gain = 0
                leftTrunc = runs[a][2] - l + 1
                rightTrunc = r - runs[b][1] + 1
                if lo == hi:
                    if runs[lo][0] == '1':
                        gain = max(gain, leftTrunc + rightTrunc)
                else:
                    if runs[lo][0] == '1':
                        gain = max(gain, leftTrunc + lengths[lo + 1])
                    if runs[hi][0] == '1':
                        gain = max(gain, rightTrunc + lengths[hi - 1])
                    if hi - lo >= 2:
                        cand = query_max(lo + 1, hi - 1)
                        gain = max(gain, cand)
            ans.append(totalOnes + gain)
        return ans