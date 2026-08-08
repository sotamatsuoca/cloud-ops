class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)
        pos = {}
        for idx in range(n):
            ch = word1[idx]
            if ch in pos:
                pos[ch].append(idx)
            else:
                pos[ch] = [idx]

        def last_le(c, bound):
            if bound < 0:
                return -1
            lst = pos.get(c)
            if not lst:
                return -1
            lo, hi = 0, len(lst) - 1
            res = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if lst[mid] <= bound:
                    res = lst[mid]
                    lo = mid + 1
                else:
                    hi = mid - 1
            return res

        def first_ge(c, lower):
            lst = pos.get(c)
            if not lst:
                return -1
            lo, hi = 0, len(lst) - 1
            res = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if lst[mid] >= lower:
                    res = lst[mid]
                    hi = mid - 1
                else:
                    lo = mid + 1
            return res

        suf0 = [0] * (m + 1)
        suf1 = [0] * (m + 1)
        suf0[m] = n
        suf1[m] = n
        for j in range(m - 1, -1, -1):
            c = word2[j]
            bound0 = suf0[j + 1] - 1
            suf0[j] = last_le(c, bound0)
            optionB = suf0[j + 1] - 1
            boundC = suf1[j + 1] - 1
            optionA = last_le(c, boundC)
            suf1[j] = optionB if optionB > optionA else optionA

        result = []
        i = 0
        b = 1
        for j in range(m):
            c = word2[j]
            kc = first_ge(c, i)
            threshold = suf1[j + 1] if b == 1 else suf0[j + 1]
            exact_ok = kc != -1 and kc + 1 <= threshold
            if exact_ok and kc == i:
                result.append(i)
                i += 1
                continue
            change_ok = b == 1 and i + 1 <= suf0[j + 1]
            if change_ok and (not exact_ok or i < kc):
                result.append(i)
                i += 1
                b = 0
                continue
            if exact_ok:
                result.append(kc)
                i = kc + 1
                continue
            return []
        return result