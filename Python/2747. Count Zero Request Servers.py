class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])

        counts = [0] * (n + 1)
        active = 0
        left = 0
        right = 0
        m = len(logs)
        result = [0] * len(queries)

        for idx in order:
            q = queries[idx]
            low = q - x

            while right < m and logs[right][1] <= q:
                server = logs[right][0]
                if counts[server] == 0:
                    active += 1
                counts[server] += 1
                right += 1

            while left < right and logs[left][1] < low:
                server = logs[left][0]
                counts[server] -= 1
                if counts[server] == 0:
                    active -= 1
                left += 1

            result[idx] = n - active

        return result