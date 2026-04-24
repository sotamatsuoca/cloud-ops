class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l_count = moves.count('L')
        r_count = moves.count('R')
        u_count = moves.count('_')
        
        return abs(l_count - r_count) + u_count