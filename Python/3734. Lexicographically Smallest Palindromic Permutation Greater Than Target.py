class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        odd_chars = [c for c in counts if counts[c] % 2 == 1]
        if n % 2 == 0:
            if len(odd_chars) != 0:
                return ""
            middle_char = None
        else:
            if len(odd_chars) != 1:
                return ""
            middle_char = odd_chars[0]

        half_count = {}
        for c, cnt in counts.items():
            h = cnt // 2
            if h:
                half_count[c] = h

        m = (n + 1) // 2
        target_half = target[:m]

        def ascending_fill(pool, length):
            chars = []
            for c in sorted(pool.keys()):
                chars.extend([c] * pool[c])
            return ''.join(chars[:length])

        def build_full(h):
            if n % 2 == 1:
                return h + h[:-1][::-1]
            return h + h[::-1]

        p = dict(half_count)
        h_chars = []
        ok = True
        for i in range(m):
            if n % 2 == 1 and i == m - 1:
                need = target_half[i]
                if middle_char == need:
                    h_chars.append(middle_char)
                else:
                    ok = False
                    break
            else:
                c = target_half[i]
                if p.get(c, 0) > 0:
                    p[c] -= 1
                    h_chars.append(c)
                else:
                    ok = False
                    break
        if ok:
            h = ''.join(h_chars)
            full = build_full(h)
            if full > target:
                return full

        states = [dict(half_count)]
        fail_pos = m
        for i in range(m):
            cur = states[i]
            if n % 2 == 1 and i == m - 1:
                need = target_half[i]
                if middle_char == need:
                    states.append(dict(cur))
                else:
                    fail_pos = i
                    break
            else:
                c = target_half[i]
                if cur.get(c, 0) > 0:
                    nxt = dict(cur)
                    nxt[c] -= 1
                    states.append(nxt)
                else:
                    fail_pos = i
                    break

        start_i = min(fail_pos, m - 1)
        for i in range(start_i, -1, -1):
            pool_state = states[i]
            if n % 2 == 1 and i == m - 1:
                if middle_char > target_half[i]:
                    prefix = target_half[:i]
                    h = prefix + middle_char
                    return build_full(h)
                else:
                    continue
            else:
                need = target_half[i]
                candidates = [c for c in pool_state if pool_state[c] > 0 and c > need]
                if not candidates:
                    continue
                cand = min(candidates)
                remaining = dict(pool_state)
                remaining[cand] -= 1
                prefix = target_half[:i]
                if n % 2 == 1:
                    fill_len = (m - 1) - (i + 1)
                    ascending_part = ascending_fill(remaining, fill_len)
                    h = prefix + cand + ascending_part + middle_char
                else:
                    fill_len = m - 1 - i
                    ascending_part = ascending_fill(remaining, fill_len)
                    h = prefix + cand + ascending_part
                return build_full(h)

        return ""