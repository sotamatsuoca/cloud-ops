class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
            robot.sort()
            factory.sort()
            
            @cache
            def dfs(robot_idx, factory_idx):
                if robot_idx == len(robot):
                    return 0
                if factory_idx == len(factory):
                    return float('inf')
                
                res = dfs(robot_idx, factory_idx + 1)
                
                current_dist = 0
                for k in range(factory[factory_idx][1]):
                    if robot_idx + k >= len(robot):
                        break
                    current_dist += abs(robot[robot_idx + k] - factory[factory_idx][0])
                    res = min(res, current_dist + dfs(robot_idx + k + 1, factory_idx + 1))
                
                return res

            return dfs(0, 0)