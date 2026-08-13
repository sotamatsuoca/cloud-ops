class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        maxX = 0
        for q in queries:
            if q[1] > maxX:
                maxX = q[1]
        n = maxX + 1
        size = 1
        while size < n:
            size *= 2

        presence = [0] * (2 * size)
        gapmax = [0] * (2 * size)

        def presence_update(pos, val):
            i = pos + size
            presence[i] = val
            i //= 2
            while i >= 1:
                presence[i] = presence[2 * i] + presence[2 * i + 1]
                i //= 2

        def gap_update(pos, val):
            i = pos + size
            gapmax[i] = val
            i //= 2
            while i >= 1:
                gapmax[i] = max(gapmax[2 * i], gapmax[2 * i + 1])
                i //= 2

        def gap_query(l, r):
            if l > r:
                return 0
            res = 0
            l += size
            r += size + 1
            while l < r:
                if l & 1:
                    res = max(res, gapmax[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res = max(res, gapmax[r])
                l //= 2
                r //= 2
            return res

        def dfs_right(node, l, r, x):
            if r <= x:
                if not presence[node]:
                    return -1
                while l < r:
                    mid = (l + r) // 2
                    if presence[2 * node + 1]:
                        node, l = 2 * node + 1, mid + 1
                    else:
                        node, r = 2 * node, mid
                return l
            if l > x:
                return -1
            mid = (l + r) // 2
            res = dfs_right(2 * node + 1, mid + 1, r, x)
            if res != -1:
                return res
            return dfs_right(2 * node, l, mid, x)

        def dfs_left(node, l, r, x):
            if l >= x:
                if not presence[node]:
                    return -1
                while l < r:
                    mid = (l + r) // 2
                    if presence[2 * node]:
                        node, r = 2 * node, mid
                    else:
                        node, l = 2 * node + 1, mid + 1
                return l
            if r < x:
                return -1
            mid = (l + r) // 2
            res = dfs_left(2 * node, l, mid, x)
            if res != -1:
                return res
            return dfs_left(2 * node + 1, mid + 1, r, x)

        def find_prev(x):
            if x < 0:
                return -1
            return dfs_right(1, 0, size - 1, x)

        def find_next(x):
            if x > size - 1:
                return -1
            return dfs_left(1, 0, size - 1, x)

        presence_update(0, 1)
        gap_update(0, 0)

        results = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                prev = find_prev(x - 1)
                nxt = find_next(x + 1)
                presence_update(x, 1)
                gap_update(x, x - prev)
                if nxt != -1:
                    gap_update(nxt, nxt - x)
            else:
                x = q[1]
                sz = q[2]
                last = find_prev(x)
                if last != -1:
                    maxGapInside = gap_query(0, last)
                    finalGap = x - last
                else:
                    maxGapInside = 0
                    finalGap = x
                results.append(max(maxGapInside, finalGap) >= sz)

        return results