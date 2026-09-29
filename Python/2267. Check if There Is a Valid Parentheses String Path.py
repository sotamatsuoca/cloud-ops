class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if (m + n - 1) % 2 == 1:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        row = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    prev = 1
                else:
                    prev = row[j]
                    if j > 0:
                        prev |= row[j - 1]
                if grid[i][j] == '(':
                    row[j] = prev << 1
                else:
                    row[j] = prev >> 1
        return (row[n - 1] & 1) == 1