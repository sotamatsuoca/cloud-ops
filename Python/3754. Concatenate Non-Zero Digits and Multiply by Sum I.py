class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = [c for c in str(n) if c != '0']
        if not s:
            return 0
        x = int("".join(s))
        sum_x = sum(int(c) for c in s)
        return x * sum_x