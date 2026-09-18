class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []
        for ch in first:
            l = first[ch]
            r = last[ch]
            valid = True
            k = l
            while k <= r:
                if first[s[k]] < l:
                    valid = False
                    break
                if last[s[k]] > r:
                    r = last[s[k]]
                k += 1
            if valid:
                intervals.append((l, r))

        intervals.sort(key=lambda x: x[1])

        res = []
        prev_end = -1
        for l, r in intervals:
            if l > prev_end:
                res.append(s[l:r + 1])
                prev_end = r

        return res