class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        ans = []
        time = 0
        for j, t in enumerate(tasks):
            time = max(time, j)
            if not free and busy and busy[0][0] > time:
                time = busy[0][0]
            while busy and busy[0][0] <= time:
                end, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))
            w, i = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, (time + t, w, i))
        return ans