class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # N, E, S, W
        curr_x, curr_y, curr_dir, max_dist_sq = 0, 0, 0, 0
        obstacle_set = {(x, y) for x, y in obstacles} # O(1) lookups
        
        for cmd in commands:
            if cmd == -2:
                curr_dir = (curr_dir - 1) % 4 # Left
            elif cmd == -1:
                curr_dir = (curr_dir + 1) % 4 # Right
            else:
                dx, dy = directions[curr_dir]
                for _ in range(cmd):
                    if (curr_x + dx, curr_y + dy) in obstacle_set: break
                    curr_x += dx
                    curr_y += dy
                max_dist_sq = max(max_dist_sq, curr_x**2 + curr_y**2)
        return max_dist_sq