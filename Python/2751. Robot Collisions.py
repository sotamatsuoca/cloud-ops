class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = []
        for i, pos in enumerate(positions):
            robots.append((pos, healths[i], directions[i], i))
        
        robots.sort()

        stack = []

        for pos, health, direction, index in robots:
            current_robot = [pos, health, direction, index]
            while stack and stack[-1][2] == 'R' and current_robot[2] == 'L' and current_robot[1] > 0:
                top_robot = stack.pop()
                if top_robot[1] > current_robot[1]:
                    top_robot[1] -= 1
                    current_robot[1] = 0
                    stack.append(top_robot)
                elif top_robot[1] < current_robot[1]:
                    current_robot[1] -= 1
                else:
                    current_robot[1] = 0
            
            if current_robot[1] > 0:
                stack.append(current_robot)
        
        stack.sort(key=lambda x: x[3])

        return [robot[1] for robot in stack]