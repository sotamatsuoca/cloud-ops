class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        litter = []
        sr = sc = -1
        for i in range(m):
            for j in range(n):
                ch = classroom[i][j]
                if ch == 'S':
                    sr, sc = i, j
                elif ch == 'L':
                    litter.append((i, j))
        L = len(litter)
        full_mask = (1 << L) - 1
        if L == 0:
            return 0
        bit_index = {}
        for idx, pos in enumerate(litter):
            bit_index[pos] = idx
        cap = energy
        E = cap + 1
        M = 1 << L
        size = m * n * E * M
        visited = bytearray(size)

        def state_index(r, c, e, mask):
            return ((r * n + c) * E + e) * M + mask

        start_idx = state_index(sr, sc, cap, 0)
        visited[start_idx] = 1
        queue = [(sr, sc, cap, 0)]
        head = 0
        moves = 0
        while head < len(queue):
            level_size = len(queue) - head
            for _ in range(level_size):
                r, c, e, mask = queue[head]
                head += 1
                if mask == full_mask:
                    return moves
                if e == 0:
                    continue
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    ch = classroom[nr][nc]
                    if ch == 'X':
                        continue
                    new_e = e - 1
                    new_mask = mask
                    if ch == 'R':
                        new_e = cap
                    elif ch == 'L':
                        b = bit_index.get((nr, nc))
                        if b is not None:
                            new_mask = mask | (1 << b)
                    idx = state_index(nr, nc, new_e, new_mask)
                    if not visited[idx]:
                        visited[idx] = 1
                        queue.append((nr, nc, new_e, new_mask))
            moves += 1
        return -1