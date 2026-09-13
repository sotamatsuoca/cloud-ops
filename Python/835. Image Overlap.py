class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        counts = {}
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                d = (r1 - r2, c1 - c2)
                counts[d] = counts.get(d, 0) + 1
        
        if not counts:
            return 0
        
        return max(counts.values())