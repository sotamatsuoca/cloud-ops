class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return ""

        count = 0
        start = 0
        specials = []

        for i, c in enumerate(s):
            count += 1 if c == '1' else -1

            if count == 0:
                specials.append('1' + self.makeLargestSpecial(s[start + 1:i]) + '0')
                start = i + 1

        return ''.join(sorted(specials, reverse=True))