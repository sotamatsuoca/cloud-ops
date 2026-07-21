class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        n = len(t)
        blocks = []
        i = 0
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            blocks.append((t[i], j - i))
            i = j
        ones = s.count('1')
        max_gain = 0
        for idx in range(1, len(blocks) - 1):
            ch, length = blocks[idx]
            if ch == '1':
                prev_ch, prev_len = blocks[idx - 1]
                next_ch, next_len = blocks[idx + 1]
                if prev_ch == '0' and next_ch == '0':
                    gain = prev_len + next_len
                    if gain > max_gain:
                        max_gain = gain
        return ones + max_gain