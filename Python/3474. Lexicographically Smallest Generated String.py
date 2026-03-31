class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        L = n + m - 1

        s = ['?'] * L
        forced = [False] * L

        for i, ch in enumerate(str1):
            if ch == 'T':
                for j in range(m):
                    p = i + j
                    c = str2[j]
                    if s[p] != '?' and s[p] != c:
                        return ""
                    s[p] = c
                    forced[p] = True

        for i in range(L):
            if s[i] == '?':
                s[i] = 'a'

        for i, ch in enumerate(str1):
            if ch == 'F' and ''.join(s[i:i + m]) == str2:
                changed = False
                for j in range(m - 1, -1, -1):
                    p = i + j
                    if not forced[p]:
                        for c in range(ord(s[p]) + 1, ord('z') + 1):
                            s[p] = chr(c)
                            if ''.join(s[i:i + m]) != str2:
                                changed = True
                                break
                        if changed:
                            break
                if not changed:
                    return ""

        return ''.join(s)