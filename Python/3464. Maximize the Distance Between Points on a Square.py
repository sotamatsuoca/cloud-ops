class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def get_pos(p):
            x, y = p
            if y == 0: return x
            if x == side: return side + y
            if y == side: return 3 * side - x
            return 4 * side - y

        def get_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        pts = sorted(points, key=get_pos)
        n = len(pts)
        pts2 = pts + pts

        def check(mid):
            for i in range(n):
                count = 1
                curr = i
                possible = True
                for _ in range(k - 1):
                    low_j, high_j = curr + 1, i + n - 1
                    next_idx = -1
                    while low_j <= high_j:
                        m_j = (low_j + high_j) // 2
                        if get_dist(pts2[curr], pts2[m_j]) >= mid:
                            next_idx = m_j
                            high_j = m_j - 1
                        else:
                            low_j = m_j + 1
                    
                    if next_idx == -1:
                        possible = False
                        break
                    curr = next_idx
                    count += 1
                
                if possible and count == k and get_dist(pts2[curr], pts2[i]) >= mid:
                    return True
            return False

        low, high = 1, 2 * side
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans