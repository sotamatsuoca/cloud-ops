class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        
        restrictions.sort()
        m = len(restrictions)
        
        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + dist)
            
        for i in range(m - 2, -1, -1):
            dist = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + dist)
            
        ans = 0
        for i in range(m - 1):
            pos_left, h_left = restrictions[i]
            pos_right, h_right = restrictions[i + 1]
            
            dist = pos_right - pos_left
            peak = (h_left + h_right + dist) // 2
            ans = max(ans, peak)
            
        return ans