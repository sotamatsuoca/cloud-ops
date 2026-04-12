class Solution:
    def minimumDistance(self, word: str) -> int:
        @functools.lru_cache(None)
        def get_dist(a, b):
            """Calculates Manhattan distance between two characters."""
            if a is None: return 0
            # Map 'A'-'Z' to 0-25
            a_idx = ord(a) - ord('A')
            b_idx = ord(b) - ord('A')
            x1, y1 = divmod(a_idx, 6)
            x2, y2 = divmod(b_idx, 6)
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(word)
        
        @functools.lru_cache(None)
        def dp(idx, f1, f2):
            if idx == n:
                return 0
            
            dist1 = get_dist(f1, word[idx]) + dp(idx + 1, word[idx], f2)
            dist2 = get_dist(f2, word[idx]) + dp(idx + 1, f1, word[idx])
            
            return min(dist1, dist2)

        return dp(0, None, None)