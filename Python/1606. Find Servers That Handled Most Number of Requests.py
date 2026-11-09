class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = list(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            start = arrival[i]

            while busy and busy[0][0] <= start:
                _, server = heapq.heappop(busy)
                insort(available, server)

            if not available:
                continue

            pos = bisect_left(available, i % k)
            if pos == len(available):
                pos = 0

            server = available.pop(pos)
            count[server] += 1
            heapq.heappush(busy, (start + load[i], server))

        best = max(count)
        return [i for i in range(k) if count[i] == best]