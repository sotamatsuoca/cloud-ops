class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, c in enumerate(s):
            total += (26 - (ord(c) - ord('a'))) * (i + 1)
        return total