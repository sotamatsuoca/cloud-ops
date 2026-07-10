class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        order = sorted(range(n), key=lambda i: nums[i])
        pos = [0] * n
        sortedVals = [0] * n
        for idx, orig in enumerate(order):
            pos[orig] = idx
            sortedVals[idx] = nums[orig]
        R = [0] * n
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j + 1 < n and sortedVals[j + 1] - sortedVals[i] <= maxDiff:
                j += 1
            R[i] = j
        LOG = max(1, n.bit_length())
        jump = [R[:]]
        for k in range(1, LOG):
            prev = jump[-1]
            cur = [prev[prev[i]] for i in range(n)]
            jump.append(cur)
        ans = []
        for u, v in queries:
            pu, pv = pos[u], pos[v]
            if pu == pv:
                ans.append(0)
                continue
            a, b = (pu, pv) if pu < pv else (pv, pu)
            cur = a
            steps = 0
            for k in range(LOG - 1, -1, -1):
                if jump[k][cur] < b:
                    cur = jump[k][cur]
                    steps += (1 << k)
            nxt = jump[0][cur]
            if nxt == cur:
                ans.append(-1)
            else:
                steps += 1
                ans.append(steps)
        return ans