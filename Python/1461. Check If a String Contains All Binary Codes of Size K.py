class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        needed = 1 << k
        if len(s) < k:
            return False

        seen = [False] * need
        mask = need - 1
        value = 0
        count = 0
    
        for i, ch in enumerate(s):
            value = ((value << 1) & mask) | (ch == '1')

            if i >= k - 1 and not seen[value]:
                seen[value] = True
                count += 1
                if count == need:
                    return True

        return False