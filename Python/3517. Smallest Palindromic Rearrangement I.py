class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        half = []
        mid = ""
        for ch in sorted(count.keys()):
            c = count[ch]
            if c % 2 == 1:
                mid = ch
            half.append(ch * (c // 2))
        half_str = "".join(half)
        return half_str + mid + half_str[::-1]