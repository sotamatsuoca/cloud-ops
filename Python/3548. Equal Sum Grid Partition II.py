class Solution:
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        top_sum = 0
        bottom_counter = Counter()
        for row in grid:
            for v in row:
                bottom_counter[v] += 1

        top_counter = Counter()

        for r in range(m - 1):
            for v in grid[r]:
                top_sum += v
                top_counter[v] += 1
                bottom_counter[v] -= 1
                if bottom_counter[v] == 0:
                    del bottom_counter[v]

            bottom_sum = total - top_sum

            if top_sum == bottom_sum:
                return True

            if top_sum > bottom_sum:
                diff = top_sum - bottom_sum
                h, w = r + 1, n

                if h >= 2 and w >= 2:
                    if diff in top_counter:
                        return True
                else:
                    if w == 1:
                        if grid[0][0] == diff or grid[r][0] == diff:
                            return True
                    else:
                        rr = 0
                        if grid[rr][0] == diff or grid[rr][n - 1] == diff:
                            return True

            else:
                diff = bottom_sum - top_sum
                h, w = m - r - 1, n

                if h >= 2 and w >= 2:
                    if diff in bottom_counter:
                        return True
                else:
                    if w == 1:
                        if grid[r + 1][0] == diff or grid[m - 1][0] == diff:
                            return True
                    else:
                        rr = m - 1
                        if grid[rr][0] == diff or grid[rr][n - 1] == diff:
                            return True

        left_sum = 0
        right_counter = Counter()
        for j in range(n):
            for i in range(m):
                right_counter[grid[i][j]] += 1

        left_counter = Counter()

        for c in range(n - 1):
            for i in range(m):
                v = grid[i][c]
                left_sum += v
                left_counter[v] += 1
                right_counter[v] -= 1
                if right_counter[v] == 0:
                    del right_counter[v]

            right_sum = total - left_sum

            if left_sum == right_sum:
                return True

            if left_sum > right_sum:
                diff = left_sum - right_sum
                h, w = m, c + 1

                if h >= 2 and w >= 2:
                    if diff in left_counter:
                        return True
                else:
                    if h == 1:
                        if grid[0][0] == diff or grid[0][c] == diff:
                            return True
                    else:
                        cc = 0
                        if grid[0][cc] == diff or grid[m - 1][cc] == diff:
                            return True

            else:
                diff = right_sum - left_sum
                h, w = m, n - c - 1

                if h >= 2 and w >= 2:
                    if diff in right_counter:
                        return True
                else:
                    if h == 1:
                        if grid[0][c + 1] == diff or grid[0][n - 1] == diff:
                            return True
                    else:
                        cc = n - 1
                        if grid[0][cc] == diff or grid[m - 1][cc] == diff:
                            return True

        return False