class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        dist = [n] * n
        
        left_pos = {}
        for i in range(2 * n):
            idx = i % n
            val = nums[idx]
            if val in left_pos:
                dist[idx] = min(dist[idx], i - left_pos[val])
            left_pos[val] = i
            
        right_pos = {}
        for i in range(2 * n - 1, -1, -1):
            idx = i % n
            val = nums[idx]
            if val in right_pos:
                dist[idx] = min(dist[idx], right_pos[val] - i)
            right_pos[val] = i
            
        return [dist[q] if dist[q] < n else -1 for q in queries]