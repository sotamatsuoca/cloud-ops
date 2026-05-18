class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i, num in enumerate(arr):
            if num not in graph:
                graph[num] = []
            graph[num].append(i)

        queue = deque([0])
        visited = {0}
        step = 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr == n - 1:
                    return step

                next_positions = []
                
                if curr - 1 >= 0 and (curr - 1) not in visited:
                    next_positions.append(curr - 1)
                    
                if curr + 1 < n and (curr + 1) not in visited:
                    next_positions.append(curr + 1)
                    
                if arr[curr] in graph:
                    for next_idx in graph[arr[curr]]:
                        if next_idx not in visited:
                            next_positions.append(next_idx)
                    del graph[arr[curr]]

                for pos in next_positions:
                    visited.add(pos)
                    queue.append(pos)

            step += 1

        return -1