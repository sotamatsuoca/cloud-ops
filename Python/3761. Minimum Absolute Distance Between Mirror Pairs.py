class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse_num(x: int) -> int:
            return int(str(x)[::-1])

        pos = {}
        min_dist = float('inf')
        
        for i, x in enumerate(nums):
            if x in pos:
                min_dist = min(min_dist, i - pos[x])
            
            pos[reverse_num(x)] = i
            
        return int(min_dist) if min_dist != float('inf') else -1