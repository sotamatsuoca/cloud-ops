class Solution:
    def processStr(self, s: str, k: int) -> str:
        m = 0
        for char in s:
            if char.islower():
                m += 1
            elif char == '*':
                m = max(0, m - 1)
            elif char == '#':
                m *= 2
            elif char == '%':
                pass

        if k >= m:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char == '*':
                m += 1
            elif char == '#':
                m //= 2
                if k >= m:
                    k -= m
            elif char == '%':
                k = m - 1 - k
            else:
                if k == m - 1:
                    return char
                m -= 1

        return '.'