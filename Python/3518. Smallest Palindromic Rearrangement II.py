class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        half_counts = {}
        mid_char = ""
        for ch, cnt in freq.items():
            if cnt % 2 == 1:
                mid_char = ch
            half_counts[ch] = cnt // 2

        half_len = n // 2
        letters = sorted(half_counts.keys())
        total_half = sum(half_counts.values())

        result = 1
        cum = 0
        for ch in letters:
            c = half_counts[ch]
            for i in range(1, c + 1):
                cum += 1
                result = result * cum // i
        total_perms = result

        if k > total_perms:
            return ""

        counts = dict(half_counts)
        remaining = total_half
        V = total_perms
        result_chars = []

        for _ in range(half_len):
            for ch in letters:
                if counts[ch] == 0:
                    continue
                candidate_V = V * counts[ch] // remaining
                if k <= candidate_V:
                    counts[ch] -= 1
                    remaining -= 1
                    V = candidate_V
                    result_chars.append(ch)
                    break
                else:
                    k -= candidate_V

        half = "".join(result_chars)
        return half + mid_char + half[::-1]